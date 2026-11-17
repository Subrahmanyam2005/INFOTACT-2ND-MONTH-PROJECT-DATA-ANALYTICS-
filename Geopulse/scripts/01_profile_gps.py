"""
GeoPulse - Week 1: GPS dataset profiling
Run: python scripts/01_profile_gps.py --gps data/gps_pings.csv --out outputs/week1
"""
import argparse
from pathlib import Path
import pandas as pd

EXPECTED = [
    "PingID", "DeviceID", "SessionID", "Latitude", "Longitude", "Timestamp",
    "AccuracyMeters", "SpeedKmh", "HeadingDegrees", "AltitudeMeters",
    "DeviceType", "MovementMode", "LocationType", "EventDate", "HourOfDay",
    "DayOfWeek", "IsWeekend", "DataSource"
]

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--gps", default="data/gps_pings.csv")
    p.add_argument("--out", default="outputs/week1")
    args = p.parse_args()
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(args.gps)
    missing_columns = [c for c in EXPECTED if c not in df.columns]

    profile = pd.DataFrame({
        "column": df.columns,
        "dtype": [str(df[c].dtype) for c in df.columns],
        "non_null_count": [int(df[c].notna().sum()) for c in df.columns],
        "null_count": [int(df[c].isna().sum()) for c in df.columns],
        "unique_count": [int(df[c].nunique(dropna=True)) for c in df.columns],
    })
    profile.to_csv(out / "gps_column_profile.csv", index=False)

    lines = [
        "GEOPULSE - GPS DATASET PROFILE",
        "=" * 40,
        f"Rows: {len(df):,}",
        f"Columns: {len(df.columns)}",
        f"Duplicate full rows: {int(df.duplicated().sum()):,}",
        f"Unique devices: {df['DeviceID'].nunique() if 'DeviceID' in df else 'N/A'}",
        f"Unique sessions: {df['SessionID'].nunique() if 'SessionID' in df else 'N/A'}",
        f"Unique pings: {df['PingID'].nunique() if 'PingID' in df else 'N/A'}",
        f"Missing expected columns: {missing_columns if missing_columns else 'None'}",
        "",
        "DATA TYPES / MISSING VALUES",
        profile.to_string(index=False),
    ]

    if "MovementMode" in df:
        lines += ["", "MOVEMENT MODE COUNTS", df["MovementMode"].value_counts(dropna=False).to_string()]
    if "DeviceType" in df:
        lines += ["", "DEVICE TYPE COUNTS", df["DeviceType"].value_counts(dropna=False).to_string()]
    if "LocationType" in df:
        lines += ["", "LOCATION TYPE COUNTS", df["LocationType"].value_counts(dropna=False).to_string()]
    if "Timestamp" in df:
        ts = pd.to_datetime(df["Timestamp"], errors="coerce")
        lines += ["", f"Timestamp parse failures: {int(ts.isna().sum()):,}",
                  f"Timestamp minimum: {ts.min()}", f"Timestamp maximum: {ts.max()}"]

    (out / "gps_profile_report.txt").write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines[:12]))
    print(f"\nSaved outputs to: {out.resolve()}")

if __name__ == "__main__":
    main()
