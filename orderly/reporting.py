"""Generate a JSON sales report from the database."""
import json
from pathlib import Path
from .database import connect


def customer_sales(db_path):
    """Return a list of dicts with customer_id, order_count, and total_amount."""
    with connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute("""
    SELECT customer_id, COUNT(*) AS order_count, SUM(amount) AS total_amount
    FROM orders
    GROUP BY customer_id
    ORDER BY total_amount DESC, customer_id
    """)
        rows = cursor.fetchall()
    return [dict(row) for row in rows]


def write_json_report(db_path, report_path):
    """Write the customer sales report to a JSON file."""
    report = customer_sales(db_path)
    Path(report_path).parent.mkdir(parents=True, exist_ok=True)
    with open(report_path, "w", encoding="utf-8") as handle:
        json.dump(report, handle, indent=2)