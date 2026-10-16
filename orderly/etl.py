"""CSV extraction, transformation, and loading workflow."""
import csv
import logging
from pathlib import Path
from .validators import validate_order

logger = logging.getLogger(__name__)


def iter_csv_rows(path: str | Path):
    """Yield rows one at a time so large input files need not fit in memory."""
    with open(path, newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            yield row


def transform_row(row: dict) -> dict:
    """Normalize the CSV row into a predictable representation."""
    return {
        "order_id": row.get("order_id", "").strip(),
        "customer_id": row.get("customer_id", "").strip(),
        "order_date": row.get("order_date", "").strip(),
        "amount": float(row.get("amount", 0))
    }


def split_valid_invalid(rows):
    """Return (valid_rows, rejected_rows); rejected rows include a reason."""
    valid, rejected = [], []
    for row in rows:
        clean = transform_row(row)
        ok, reason = validate_order(clean)
        if ok:
            valid.append(clean)
        else:
            rejected.append({"row": row, "reason": reason})
    return valid, rejected


def import_csv(path, database):
    """Import valid rows and return counts. Implement after database layer."""
    rows = iter_csv_rows(path)
    valid, rejected = split_valid_invalid(rows)
    # TODO: implement database insertion logic
    return {"loaded": len(valid), "rejected": len(rejected)}
