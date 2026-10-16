-- Task A: total order count and revenue per customer.
SELECT
    customer_id,
    COUNT(*) AS order_count,
    SUM(amount) AS total_amount
FROM orders
GROUP BY customer_id
ORDER BY customer_id;

-- Task B: customers who have never placed an order (NOT EXISTS or LEFT JOIN).
SELECT
    c.customer_id
FROM customers AS c
WHERE NOT EXISTS (
    SELECT 1
    FROM orders AS o
    WHERE o.customer_id = c.customer_id
)
ORDER BY c.customer_id;

-- Task C: rank orders by amount within each customer (RANK / ROW_NUMBER).
SELECT
    order_id,
    customer_id,
    order_date,
    amount,
    RANK() OVER (
        PARTITION BY customer_id
        ORDER BY amount DESC
    ) AS amount_rank,
    ROW_NUMBER() OVER (
        PARTITION BY customer_id
        ORDER BY amount DESC, order_id
    ) AS amount_row_number
FROM orders
ORDER BY customer_id, amount DESC, order_id;

-- Task D: inspect a date-filtered query with EXPLAIN QUERY PLAN.
EXPLAIN QUERY PLAN
SELECT
    order_id,
    customer_id,
    order_date,
    amount
FROM orders
WHERE order_date >= '2026-10-01'
  AND order_date < '2026-11-01'
ORDER BY order_date, order_id;
