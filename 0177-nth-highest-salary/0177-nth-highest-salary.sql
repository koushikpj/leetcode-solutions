create function getNthHighestSalary(n int) returns int
begin
declare var int; 
set var = n-1; 
  return (
      select distinct salary from employee 
      order by salary desc limit 1 offset var );
end