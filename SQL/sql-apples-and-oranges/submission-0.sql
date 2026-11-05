-- Write your query below

SELECT a.sale_date, a.sold_num - o.sold_num AS diff FROM sales as a JOIN sales as o ON o.sale_date = a.sale_date WHERE a.fruit = 'apples' AND o.fruit = 'oranges' ORDER BY a.sale_date;