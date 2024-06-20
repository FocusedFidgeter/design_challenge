## Convert SQL queries to ORM

SQL queries and SQLAlchemy ORM queries are two ways of querying relational databases, but they differ in their syntax 
and approach. 

SQL queries involve writing SQL statements directly in the code to retrieve data from the database. On the other hand, 
SQLAlchemy ORM queries are written in Python and use an object-oriented approach to interact with the database. 
Rather than writing SQL statements, developers define classes and their attributes that map to database tables and 
columns. These classes are known as ORM models, and they provide an abstraction layer between the application code 
and the database.

In summary, while SQL queries require knowledge of SQL syntax and are more focused on the database structure, 
SQLAlchemy ORM queries provide a higher level of abstraction and can make database interactions more intuitive and 
Pythonic.



## Challenge

For this challenge you need to convert the SQL queries / syntax in the event api application to ORM. At the end of the 
conversion, there should be no SQL code directly written as string inside the code of the api application. You also need 
to create the database, and insert the tables in the ORM way. 

### Hint
Make sure to completely stop the api local server after running the `run.py` script.









