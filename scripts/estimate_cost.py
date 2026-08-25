#!/usr/bin/env python3
"""Estimate request count and spend from PawDirector's cost-plan CSV."""

import argparse
import csv
import math
from decimal import Decimal


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_path")
    args = parser.parse_args()
    total = Decimal("0")
    with open(args.csv_path, newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    for row in rows:
        blocks = int(row["blocks"])
        candidates = int(row["candidates"])
        retry_factor = Decimal(row["retry_factor"])
        requests = math.ceil(Decimal(blocks * candidates) * retry_factor)
        cost = Decimal(row["unit_price"]) * requests
        row["expected_requests"] = str(requests)
        row["expected_cost"] = f"{cost:.4f}"
        total += cost
        print(f'{row["route_id"]}: {requests} requests, {cost:.4f} {row["currency"]}')
    currencies = {row["currency"] for row in rows}
    if len(currencies) == 1:
        print(f"TOTAL: {total:.4f} {currencies.pop()}")
    else:
        print("TOTAL omitted: multiple currencies")


if __name__ == "__main__":
    main()
