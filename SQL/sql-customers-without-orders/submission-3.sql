-- Write your query below

-- Implementation 1: IN operation

--SELECT name FROM customers WHERE id NOT IN (SELECT customer_id FROM orders);

-- Implementation 2: EXISTS operation[Safer to avoid UNKNOWN value errors]
--SELECT c.name FROM customers as c WHERE NOT EXISTS (SELECT 1 FROM orders as o WHERE o.customer_id = c.id);

-- Implementation 3: LEFT Join
SELECT c.name
FROM customers AS c
LEFT JOIN orders AS o 
    ON c.id = o.customer_id
WHERE o.id IS NULL; -- There is no match when the LEFT JOIN returns null as o.id so that means this is the customer name we need to return.
