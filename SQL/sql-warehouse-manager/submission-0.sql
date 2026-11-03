-- Write your query below

SELECT w.name as warehouse_name, SUM(w.units * p.width * p.length * p.height) as volume FROM warehouse as w JOIN products as p ON p.product_id = w.product_id GROUP BY w.name;