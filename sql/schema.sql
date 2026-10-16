CREATE TABLE IF NOT EXISTS customers (
    customer_id TEXT PRIMARY KEY NOT NULL
);

CREATE TABLE IF NOT EXISTS orders (
    order_id TEXT PRIMARY KEY NOT NULL UNIQUE,
    customer_id TEXT NOT NULL,
    order_date TEXT NOT NULL,
    amount REAL NOT NULL CHECK (amount > 0)
);

CREATE INDEX IF NOT EXISTS idx_orders_order_date
    ON orders (order_date);
