-- https://leetcode.com/problems/combine-two-tables/
-- Write your PostgreSQL query statement below
SELECT p.firstName,
    p.lastName,
    a.city,
    a.state
FROM Person p
    LEFT JOIN Address a USING(personId);