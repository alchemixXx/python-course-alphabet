# PLAN OF THE LECTION

# SQL basic commands

### Introduction into PosgreSQL

- Console client psql
    - Create user with password
    - Create database
    - Grant all privileges to the db for created user

### Data structure

- create/delete databases

- create/delete tables

- Data types in PostgreSQL

- Column and table constraints

- External keys

- Change tables


### Data operations

- INSERT

- SELECT

- WHERE

- UPDATE

- DELETE


### Requests

- DISTINCT. Selection of unique values

- ORDER BY. Sorting

- GROUP BY

- HAVING

- Getting a range of lines. LIMIT and OFFSET

- Filter operators

- Aggregate functions

- Subqueries


### Joining Tables

- Implicit table join

- INNER JOIN

- OUTER JOIN and CROSS JOIN

- Grouping in compounds

- Union of sets. UNION

- Set difference. EXCEPT

- Intersection of many. INTERSECT

# Integration with python

### PyCharm configuration

### Migration

### Fixtures

### Tests

# Useful information

How to configure your Postgres environment

https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-18-04

Same information for those one who does not like English (yet) 

https://timeweb.com/ru/community/articles/kak-ustanovit-postgresql-na-ubuntu-18-04-1 

> - sudo -u postgres psql
> - postgres=# create database cursor_db;
> - postgres=# create user cursor with encrypted password 'very_secret_password';
> - postgres=# grant all privileges on database cursor_db to cursor;
> - postgres=# \q;
  

From linux shell
    psql -h localhost -U cursor -d cursor_db -p 5433 ( or 5432 based on your version of OS)


If you catch this error installing psycopg2 in your virtual env
```
    Error: b'You need to install postgresql-server-dev-X.Y for building a server-side extension or libpq-dev for building a client-side application.\n'
``` 

Running next commands could fix your problem 

```
sudo apt-get install postgresql
sudo apt-get install python-psycopg2
sudo apt-get install libpq-dev
sudo apt-get install python3.7-dev

```


 When you are in psql command line type
```.postgres=# 

\help
\?

```
to see all possible commands

About basic commands in psql you could read here 
http://www.postgresqltutorial.com/psql-commands/


If you could connect to database with this command
```
psql -h localhost -d cursor_db -U cursor -p 5433

```

But still could not connect with python code 
```
subl /etc/postgresql/9.6/main/pg_hba.conf
```
and change `local all all peer` to `local all all password`
