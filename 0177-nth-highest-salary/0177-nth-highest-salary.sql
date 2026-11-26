CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
declare var int;
set var = n-1;
  RETURN (
      select distinct salary from employee 
      order by salary desc limit 1 offset var

  );
END