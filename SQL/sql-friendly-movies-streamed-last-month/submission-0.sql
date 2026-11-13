-- Write your query below

SELECT DISTINCT c.title FROM content as c  INNER JOIN tv_program as t ON t.content_id = c.content_id AND t.program_date LIKE '2020-06%' WHERE kids_content = 'Y' AND content_type = 'Movies';