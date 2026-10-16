from sqlalchemy import true

from orderly.validators import validate_order


def test_valid_order_is_accepted():
    row = {"order_id": "O-100", "customer_id": "C-1", "order_date": "2026-10-01", "amount": "12.50"}
    assert validate_order(row) == (True, "")


def test_missing_order_id_is_rejected():
    row = {"order_id": "", "customer_id": "C-1", "order_date": "2026-10-01", "amount": "12.50"}
    ok, reason = validate_order(row)
    assert not ok
    assert "order_id" in reason.lower()


def test_negative_amount_is_rejected():
    row = {"order_id": "O-2", "customer_id": "C-1", "order_date": "2026-10-01", "amount": "-1"}
    assert validate_order(row)[0] is False   # TODO: implement amount validation to reject negative values
