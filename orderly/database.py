"""SQLite persistence layer. Complete the TODOs."""
import sqlite3
from pathlib import Path

SCHEMA = """
CREATE TABLE IF NOT EXISTS orders (
    order_id TEXT PRIMARY KEY,
    customer_id TEXT NOT NULL,
    order_date TEXT NOT NULL,
    amount REAL NOT NULL
);
"""


def connect(db_path):
    Path(db_path).parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(db_path)
    connection.row_factory = sqlite3.Row
    return connection


def initialize(db_path):
    """Create the database schema if it does not already exist."""
    with connect(db_path) as conn:
        conn.executescript(SCHEMA)
        return conn  # return the connection for testing purposes


def insert_orders(db_path, rows):
    """Insert rows into the orders table, ignoring duplicates. Return count inserted."""
    with connect(db_path) as conn:
        cursor = conn.cursor()
    
    cursor.executemany("""
        INSERT OR IGNORE INTO orders (order_id, customer_id, order_date, amount)
        VALUES (:order_id, :customer_id, :order_date, :amount)
    """, rows)
    conn.commit()
    return cursor.rowcount

    raise NotImplementedError("Complete idempotent insertion")
