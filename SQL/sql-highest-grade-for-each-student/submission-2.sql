-- Write your query below

-- Using Window Functions
-- WITH ranked_scores AS (
--     SELECT student_id, exam_id, score, ROW_NUMBER() OVER (
--         PARTITION BY student_id
--         ORDER BY score DESC, exam_id ASC
--     ) AS rn
--     FROM exam_results
-- )

-- SELECT student_id, exam_id, score
-- FROM ranked_scores
-- WHERE rn = 1
-- ORDER BY student_id ASC;

-- Using PostgreSQL Distinct ON, Easiest tho

SELECT DISTINCT ON (Student_id) student_id, exam_id, score FROM exam_results ORDER BY student_id ASC, score DESC, exam_id ASC;