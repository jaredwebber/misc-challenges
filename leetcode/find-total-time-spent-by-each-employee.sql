-- https://leetcode.com/problems/find-total-time-spent-by-each-employee
SELECT
    event_day AS DAY,
    emp_id,
    SUM(out_time - in_time) AS total_time
FROM
    Employees
GROUP BY
    event_day,
    emp_id;