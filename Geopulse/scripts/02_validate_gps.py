"""
GeoPulse - Week 1: GPS data quality checks
Run: python scripts/02_validate_gps.py --gps data/gps_pings.csv --out outputs/week1
Boundary is the simulated Visakhapatnam bounding box used for this dataset.
"""
import argparse
from pathlib import Path
import pandas as pd

LAT_MIN, LAT_MAX = 17.6468, 17.7268
LON_MIN, LON_MAX = 83.1785, 83.2585

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--gps", default="data/gps_pings.csv")
    p.add_argument("--out", default="outputs/week1")
    args = p.parse_args()
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(args.gps)
    required = ["PingID", "DeviceID", "SessionID", "Latitude", "Longitude",
                "Timestamp", "AccuracyMeters", "SpeedKmh", "HeadingDegrees",
                "AltitudeMeters", "MovementMode"]
    missing_cols = [c for c in required if c not in df.columns]
    if missing_cols:
        raise ValueError(f"Missing required columns: {missing_cols}")

    checks = []
    def add(name, count, severity="WARNING", note=""):
        checks.append({"check": name, "issue_count": int(count),
                       "status": "PASS" if int(count) == 0 else severity,
                       "note": note})

    add("Missing values in required columns",
        df[required].isna().any(axis=1).sum(),
        note="Rows with at least one missing required value")
    add("Duplicate PingID", df["PingID"].duplicated(keep=False).sum(),
        note="Rows participating in duplicate PingID values")
    add("Duplicate full rows", df.duplicated().sum())

    lat = pd.to_numeric(df["Latitude"], errors="coerce")
    lon = pd.to_numeric(df["Longitude"], errors="coerce")
    add("Invalid/missing latitude or longitude", (lat.isna() | lon.isna()).sum())
    add("Coordinates outside simulated boundary",
        ((lat < LAT_MIN) | (lat > LAT_MAX) | (lon < LON_MIN) | (lon > LON_MAX)).sum(),
        note=f"Expected lat {LAT_MIN}-{LAT_MAX}, lon {LON_MIN}-{LON_MAX}")

    numeric_rules = {
        "AccuracyMeters": (0, 1000),
        "SpeedKmh": (0, 200),
        "HeadingDegrees": (0, 360),
        "AltitudeMeters": (-500, 9000),
    }
    for col, (lo, hi) in numeric_rules.items():
        values = pd.to_numeric(df[col], errors="coerce")
        add(f"{col} outside plausible validation range",
            (values.isna() | (values < lo) | (values > hi)).sum(),
            note=f"Accepted screening range: {lo} to {hi}; review exceptions")

    ts = pd.to_datetime(df["Timestamp"], errors="coerce")
    add("Timestamp parse failures", ts.isna().sum())
    add("Rows with timestamp outside November 2026 simulation week",
        ((ts < pd.Timestamp("2026-11-02")) |
         (ts >= pd.Timestamp("2026-11-09")) | ts.isna()).sum(),
        note="Expected timestamps from 2026-11-02 through 2026-11-08")

    allowed_modes = {"Walking", "Driving", "Cycling", "Stationary"}
    if "MovementMode" in df:
        add("Unknown MovementMode values",
            (~df["MovementMode"].isin(allowed_modes)).sum(),
            note=f"Expected categories: {sorted(allowed_modes)}")

    report = pd.DataFrame(checks)
    report.to_csv(out / "gps_validation_checks.csv", index=False)

    # Device-level record counts help verify the intended 100 pings per device.
    device_counts = df.groupby("DeviceID").size().rename("ping_count").reset_index()
    device_counts.to_csv(out / "gps_device_ping_counts.csv", index=False)

    print(report.to_string(index=False))
    print(f"\nDevices found: {df['DeviceID'].nunique():,}")
    print(f"Sessions found: {df['SessionID'].nunique():,}")
    print(f"Ping rows: {len(df):,}")
    print(f"Devices not having exactly 100 rows: {(device_counts['ping_count'] != 100).sum():,}")
    print(f"\nSaved outputs to: {out.resolve()}")

if __name__ == "__main__":
    main()
