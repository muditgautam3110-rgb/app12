"""Command-line entry point for the Orderly practice project."""
import argparse
import logging
from .etl import import_csv
from .reporting import write_json_report


def main():
    parser = argparse.ArgumentParser(description="Import sales orders and generate a report")
    parser.add_argument("--input", required=True)
    parser.add_argument("--db", required=True)
    parser.add_argument("--report", required=True)
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    result = import_csv(args.input, args.db)
    write_json_report(args.db, args.report)
    print(f"Loaded {result['loaded']} orders; rejected {result['rejected']} rows")


if __name__ == "__main__":
    main()
