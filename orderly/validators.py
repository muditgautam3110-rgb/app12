"""Validation helpers for order records. Complete the TODOs."""
from datetime import date
from decimal import Decimal, InvalidOperation


def validate_order(row: dict) -> tuple[bool, str]:
    """Return (is_valid, reason). Empty reason means the row is valid."""
    if not str(row.get("order_id") or "").strip():
        return False, "Missing order_id"
    if not str(row.get("customer_id") or "").strip():
        return False, "Missing customer_id"
    order_date = str(row.get("order_date") or "").strip()
    if not order_date:
        return False, "Missing order_date"
    try:
        parsed_date = date.fromisoformat(order_date)
    except ValueError:
        return False, "Invalid order_date; expected YYYY-MM-DD"
    if parsed_date.isoformat() != order_date:
        return False, "Invalid order_date; expected YYYY-MM-DD"

    amount_value = row.get("amount")
    if amount_value is None or not str(amount_value).strip():
        return False, "Missing amount"
    try:
        amount = Decimal(str(amount_value))
    except (InvalidOperation, ValueError):
        return False, "Invalid amount; expected a positive number"
    if not amount.is_finite() or amount <= 0:
        return False, "Invalid amount; must be greater than zero"
    return True, ""
