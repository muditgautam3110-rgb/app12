from pathlib import Path
from orderly.etl import iter_csv_rows, split_valid_invalid

DATA = Path(__file__).parents[1] / "data" / "orders.csv"


def test_csv_generator_reads_all_rows():
    rows = list(iter_csv_rows(DATA))
    assert len(rows) == 8
    assert rows[0]["order_id"] == "O-1001"


def test_invalid_rows_are_rejected():
    rows = [
        {"order_id": "O-1", "customer_id": "C-1", "order_date": "2026-10-01", "amount": "10.00"},
        {"order_id": "", "customer_id": "C-2", "order_date": "2026-10-01", "amount": "20.00"},
    ]
    valid, rejected = split_valid_invalid(rows)
    assert len(valid) == 1
    assert len(rejected) == 1
