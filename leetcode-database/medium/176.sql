-- https://leetcode.com/problems/second-highest-salary/
-- Write your PostgreSQL query statement below
SELECT (
        SELECT DISTINCT salary
        FROM Employee
        ORDER BY salary DESC OFFSET 1
        LIMIT 1
    ) SecondHighestSalary;