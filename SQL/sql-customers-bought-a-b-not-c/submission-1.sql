-- Write your query below

-- Aggregate Functions with Group By Solution - less Code but complex, postgres doesnt support boolean sum functions like this so we assign the type

-- SELECT c.customer_id, c.customer_name FROM customers as c WHERE c.customer_id IN (SELECT o.customer_id FROM orders as o GROUP BY o.customer_id HAVING SUM((o.product_name = 'C')::int) = 0 AND SUM((o.product_name = 'A')::int) > 0 AND SUM((o.product_name = 'B')::int) > 0) ORDER BY c.customer_name;


-- Easier solution is, multiple subqueries

SELECT c.customer_id, c.customer_name
FROM customers c
WHERE c.customer_id IN (
    SELECT customer_id FROM orders WHERE product_name = 'A'
)
AND c.customer_id IN (
    SELECT customer_id FROM orders WHERE product_name = 'B'
)
AND c.customer_id NOT IN (
    SELECT customer_id FROM orders WHERE product_name = 'C'
)
ORDER BY c.customer_name;
