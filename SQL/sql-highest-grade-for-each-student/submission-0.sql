-- Write your query below

-- Using PostgreSQL Distint ON

SELECT DISTINCT ON (Student_id) student_id, exam_id, score FROM exam_results ORDER BY student_id ASC, score DESC, exam_id ASC;