# GROUP BY

## Contents

 - [Intro to GROUP BY clause](#intro)
 - [GROUP BY with COUNT() function](#count)
 - [GROUP BY with SUM() function](#sum)
 - [GROUP BY on more than one columns](#many-columns)
 - [GROUP BY with WHERE clause](#where-clause)

---

<div id="intro"></div>

## Intro to GROUP BY clause

> The usage of SQL GROUP BY clause is, to divide the rows in a table into smaller groups.

For example, see image below:

![img](images/OfrOY.png)  

**NOTE:**  
The GROUP BY clause is used with the SQL SELECT statement.

---

<div id="count"></div>

## GROUP BY with COUNT() function

The following query displays number of employees work in each department:

**INPUT:**  
```sql
SELECT department_id  as "Department Code",
COUNT(*) as "No of Employees"
FROM employees
GROUP BY department_id;
```

**OUTPUT:**  
```sql
+-----------------+-----------------+
| Department Code | No of Employees |
+-----------------+-----------------+
|              90 |               3 |
|              60 |               5 |
|             100 |               6 |
|              30 |               6 |
|              50 |              45 |
|              80 |              35 |
|              10 |               1 |
|              20 |               2 |
|              40 |               1 |
|              70 |               1 |
|             110 |               2 |
+-----------------+-----------------+
```

---

<div id="sum"></div>

## GROUP BY with SUM() function

The following query displays total salary paid to employees work in each department:

**INPUT:**  
```sql
SELECT department_id, SUM(salary)
FROM employees
GROUP BY department_id;
```

**OUTPUT:**  
```sql
+---------------+-------------+
| department_id | SUM(salary) |
+---------------+-------------+
|            90 |       58000 |
|            60 |       28800 |
|           100 |       51600 |
|            30 |       24900 |
|            50 |      156400 |
|            80 |      311500 |
|            10 |        4400 |
|            20 |       19000 |
|            40 |        6500 |
|            70 |       10000 |
|           110 |       20300 |
+---------------+-------------+
```

Now, the following query displays number of employees, total salary paid to employees work in each department:

**INPUT:**  
```sql
SELECT department_id as "Department Code",
COUNT(*) as "No of Employees",
SUM(salary) as "Total Salary"
FROM employees
GROUP BY department_id;
```

**OUTPUT:**  
```sql
+-----------------+-----------------+--------------+
| Department Code | No of Employees | Total Salary |
+-----------------+-----------------+--------------+
|              90 |               3 |        58000 |
|              60 |               5 |        28800 |
|             100 |               6 |        51600 |
|              30 |               6 |        24900 |
|              50 |              45 |       156400 |
|              80 |              35 |       311500 |
|              10 |               1 |         4400 |
|              20 |               2 |        19000 |
|              40 |               1 |         6500 |
|              70 |               1 |        10000 |
|             110 |               2 |        20300 |
+-----------------+-----------------+--------------+
```

---

<div id="many-columns"></div>

## GROUP BY on more than one columns

The following query displays the **department code**, **job id**, **total salary paid** to employees **group by** <u>department_id</u>, <u>job_id</u>:

**INPUT:**  
```sql
SELECT department_id as "Department Code",
job_id,
SUM(salary) as "Total Salary"
FROM employees
GROUP BY department_id, job_id;
```

**OUTPUT:**  
```sql
+-----------------+------------+--------------+
| Department Code | job_id     | Total Salary |
+-----------------+------------+--------------+
|              90 | AD_PRES    |        24000 |
|              90 | AD_VP      |        34000 |
|              60 | IT_PROG    |        28800 |
|             100 | FI_MGR     |        12000 |
|             100 | FI_ACCOUNT |        39600 |
|              30 | PU_MAN     |        11000 |
|              30 | PU_CLERK   |        13900 |
|              50 | ST_MAN     |        36400 |
|              50 | ST_CLERK   |        55700 |
|              80 | SA_MAN     |        61000 |
|              80 | SA_REP     |       250500 |
|              50 | SH_CLERK   |        64300 |
|              10 | AD_ASST    |         4400 |
|              20 | MK_MAN     |        13000 |
|              20 | MK_REP     |         6000 |
|              40 | HR_REP     |         6500 |
|              70 | PR_REP     |        10000 |
|             110 | AC_MGR     |        12000 |
|             110 | AC_ACCOUNT |         8300 |
+-----------------+------------+--------------+
```

---

<div id="where-clause"></div>

## GROUP BY with WHERE clause

The following query displays the **department code**, **total salary paid** to employees **group by** <u>department_id</u> and <u>manager_id=103</u>:

**INPUT:**  
```sql
SELECT department_id as "Department Code", 
SUM(salary) as "Total Salary" 
FROM  employees 
WHERE MANAGER_ID = 103
GROUP BY department_id;
```

**OUTPUT:**  
```sql
+-----------------+--------------+
| Department Code | Total Salary |
+-----------------+--------------+
|              60 |        19800 |
+-----------------+--------------+
```

---

**REFERENCES:**  
[SQL GROUP BY clause](https://www.w3resource.com/sql/group-by.php)  

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
