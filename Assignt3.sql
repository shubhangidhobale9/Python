create database EmployeeDetails
use EmployeeDetails

create table EmployeeDetails(
Empid int,
FullName Varchar(50),
Managerid int,
DateOfJoining Date,
City Varchar(50))

select * from EmployeeDetails

create table EmployeeSalary(
Empid int,
Project varchar(50),
Salary int,
Variable int)
select * from EmployeeDetails
select * from EmployeeSalary

/*Q1)SQL Query to fetch records that are present in one table but not in another table.*/

select * from EmployeeDetails 
MINUS
select * from EmployeeSalary

/*Q2)SQL query to fetch all the employees who are not working on any project.*/
select Empid from EmployeeSalary
where Project IS NULL


/*Q3)SQL query to fetch all the Employees from EmployeeDetails who joined in the Year 2020.*/
select * from EmployeeDetails
Where DateOfJoining=2020/01/30

/*Q4)Fetch all employees from EmployeeDetails who have a salary record in EmployeeSalary.*/
select * from EmployeeDetails E
Where Exists
(select * from EmployeeSalary S
Where E.Empid= S.Empid);

/*Q5)Write an SQL query to fetch a project-wise count of employees.*/
 select Project,COUNT(Empid) EmpProjectCount
 from EmployeeSalary
 Group by Project

 select * from EmployeeDetails
select * from EmployeeSalary

/*6)Fetch employee names and salaries even if the salary value is not present for the employee.*/
select E.FullName,S.Salary
From EmployeeDetails E
Left Join
EmployeeSalary S
on E.Empid = S.Empid

/*Q7)Write an SQL query to fetch all the Employees who are also managers.*/
select DISTINCT E.FullName
From EmployeeDetails E
Inner Join EmployeeDetails M
on E.Empid = M.Managerid

/*Q8)Write an SQL query to fetch duplicate records from EmployeeDetails.*/
select FullName,Managerid,DateOfJoining,City,COUNT(*)
From EmployeeDetails
Group by FullName,Managerid,DateOfJoining,City
Having COUNT(*)>1

/*Q9)Write an SQL query to fetch only odd rows from the table*/
select * from EmployeeDetails
where MOD (Empid, 2) <>0

/*Q10)Write a query to find the 3rd highest salary from a table without top or limit keyword.*/


select * from EmployeeDetails
select * from EmployeeSalary

SELECT  MAX(Salary) from EmployeeSalary
WHERE Salary <>
(SELECT MAX(Salary) from EmployeeSalary)
(SELECT MAX(Salary)as salary from EmployeeSalary)







