-- Write your query below

SELECT c.customer_id, c.customer_name FROM customers as c WHERE c.customer_id IN (SELECT o.customer_id FROM orders as o GROUP BY o.customer_id HAVING SUM((o.product_name = 'C')::int) = 0 AND SUM((o.product_name = 'A')::int) > 0 AND SUM((o.product_name = 'B')::int) > 0) ORDER BY c.customer_name;