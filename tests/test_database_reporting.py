from pathlib import Path
import pytest
from orderly.database import initialize, insert_orders
from orderly.reporting import customer_sales


@pytest.fixture
def db_path(tmp_path):
    path = tmp_path / "orders.db"
    initialize(path)
    return path


def test_insert_is_idempotent(db_path):
    rows = [{"order_id": "O-1", "customer_id": "C-1", "order_date": "2026-10-01", "amount": 10.0}]
    assert insert_orders(db_path, rows) == 1
    assert insert_orders(db_path, rows) == 0


def test_customer_sales_aggregates(db_path):
    rows = [
        {"order_id": "O-1", "customer_id": "C-1", "order_date": "2026-10-01", "amount": 10.0},
        {"order_id": "O-2", "customer_id": "C-1", "order_date": "2026-10-02", "amount": 15.0},
    ]
    insert_orders(db_path, rows)
    report = customer_sales(db_path)
    assert report == [{"customer_id": "C-1", "order_count": 2, "total_amount": 25.0}]
