"""
GeoPulse - Week 1: Store reference dataset profiling and validation
Run: python scripts/03_validate_stores.py --stores data/stores.csv --out outputs/week1
"""
import argparse
from pathlib import Path
import pandas as pd

LAT_MIN, LAT_MAX = 17.6468, 17.7268
LON_MIN, LON_MAX = 83.1785, 83.2585

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--stores", default="data/stores.csv")
    p.add_argument("--out", default="outputs/week1")
    args = p.parse_args()
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(args.stores)
    required = ["StoreID", "StoreName", "StoreCategory", "Latitude", "Longitude",
                "City", "OpeningTime", "ClosingTime", "IsActive"]
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    lat = pd.to_numeric(df["Latitude"], errors="coerce")
    lon = pd.to_numeric(df["Longitude"], errors="coerce")
    checks = [
        ("Missing values in required columns", df[required].isna().any(axis=1).sum()),
        ("Duplicate StoreID", df["StoreID"].duplicated(keep=False).sum()),
        ("Invalid/missing coordinates", (lat.isna() | lon.isna()).sum()),
        ("Coordinates outside simulated boundary",
         ((lat < LAT_MIN) | (lat > LAT_MAX) | (lon < LON_MIN) | (lon > LON_MAX)).sum()),
    ]
    report = pd.DataFrame(checks, columns=["check", "issue_count"])
    report["status"] = report["issue_count"].map(lambda n: "PASS" if n == 0 else "WARNING")
    report.to_csv(out / "store_validation_checks.csv", index=False)

    df["StoreCategory"].value_counts(dropna=False).rename_axis("StoreCategory").reset_index(
        name="store_count"
    ).to_csv(out / "store_category_counts.csv", index=False)

    print(f"Store records: {len(df):,}")
    print(f"Unique Store IDs: {df['StoreID'].nunique():,}")
    print(report.to_string(index=False))
    print(f"\nSaved outputs to: {out.resolve()}")

if __name__ == "__main__":
    main()
