-- https://leetcode.com/problems/nth-highest-salary/
CREATE OR REPLACE FUNCTION NthHighestSalary(N INT) RETURNS TABLE (Salary INT) AS $$
DECLARE N_OFF INT;
BEGIN IF N > 0 THEN
SELECT N -1 INTO N_OFF;
ELSE RETURN QUERY(
    SELECT null::INT
);
RETURN;
END IF;
RETURN QUERY (
    SELECT (
            SELECT DISTINCT Employee.salary
            FROM Employee
            ORDER BY Employee.salary DESC OFFSET N_OFF
            LIMIT 1
        )
);
END;
$$ LANGUAGE plpgsql;