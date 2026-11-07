-- Write your query below

-- Using Greatest and Least
--SELECT LEAST(from_id, to_id) as person1, GREATEST(to_id, from_id) as person2, COUNT(*) as call_count, SUM(duration) as total_duration FROM calls GROUP BY LEAST(from_id, to_id), GREATEST(to_id, from_id);

-- Using Union
WITH organised_table AS (
    -- Keep from_id first when it is smaller
    SELECT from_id, to_id, duration
    FROM calls
    WHERE from_id < to_id
    UNION ALL
    -- Swap to_id to the front when it is smaller
    SELECT to_id, from_id, duration
    FROM calls
    WHERE to_id < from_id
)

SELECT from_id as person1, to_id as person2, COUNT(*) as call_count, SUM(duration) as total_duration FROM organised_table GROUP BY from_id, to_id;