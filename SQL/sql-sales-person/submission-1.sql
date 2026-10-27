-- Write your query below

SELECT s.name FROM sales_person as s where s.sales_id NOT IN (SELECT o.sales_id FROM orders as o LEFT JOIN company as c ON c.com_id = o.com_id WHERE c.name = 'CRIMSON');