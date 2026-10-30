#!/usr/bin/env python3
import argparse
import csv
import json
import re
import sys
from pathlib import Path

def validate_ad_copy(csv_path, bounds_path, out_csv):
    with open(bounds_path, "r", encoding="utf-8") as f:
        bounds = json.load(f)

    max_discount = bounds.get("max_allowable_discount_percent", 30)
    banned_claims = bounds.get("prohibited_claims", [])

    flagged = []
    with open(csv_path, "r", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            text = r.get("copy_text", "")
            # Check fabricated discount percentages
            discounts = [int(x) for x in re.findall(r'(\d+)%', text)]
            for d in discounts:
                if d > max_discount:
                    flagged.append({"copy_text": text, "violation": f"Hallucinated discount {d}% exceeds allowed max of {max_discount}%"})

            for claim in banned_claims:
                if claim in text:
                    flagged.append({"copy_text": text, "violation": f"Unauthorized claim: '{claim}'"})

    with open(out_csv, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["copy_text", "violation"])
        writer.writeheader()
        writer.writerows(flagged)
    return len(flagged)

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--csv", required=True)
    p.add_argument("--bounds", default="config/authorized_offer_bounds.sample.json")
    p.add_argument("--out", default="reports/flagged_claims_report.csv")
    args = p.parse_args()

    c = validate_ad_copy(args.csv, args.bounds, args.out)
    print(f"Audited AI copy: {c} unauthorized claims flagged -> {args.out}")

if __name__ == "__main__":
    main()
