# coding-test

## Technical Backend Developer Test

1. Problem: Given the following SQL tables

payments_table
```
id: Integer
payment_date: Timestamp
contract_id: Integer
amount: Float
```


contracts_table
```
id: Integer
start_date: Timestamp
product_id: Integer
```


user_table
```
id: integer
date_joined: Timestamp
username: Varchar
```


Retrieve all users with date_joined of today, the number of contracts each user has, and the number of contracted cases (a case is contracted if it has at least one payment) using SQL Language.

1. Solution:

The relationship between contracts and users is missing. This relationship is necessary to execute the query.
Assuming that the relationship is expressed as in the table below:

contracts_table
```
id: Integer
start_date: Timestamp
product_id: Integer
user_id: Integer
```

we could execute the query in the following way

* Clone repository

```
git clone git@github.com:sanjmen/coding-test.git
cd coding-test
```

* Create a virtualenv

```
python3 -m venv myenv
source myenv/bin/activate
```

* Install requirements

```
pip install -r sql-query/requirements.txt
```

* Run docker container with postgresql db

```
docker-compose build && docker-compose up db -d
```

* Create tables and Populate db

```
python sql-query/populate_db.py
```

returns:
```
INFO:__main__:Starting data import process...
INFO:__main__:Dropping tables in database...
INFO:__main__:Creating tables in database...
INFO:__main__:Importing data into tables...
INFO:__main__:Importing data from users.csv to users table...
INFO:__main__:Importing data from contracts.csv to contracts table...
INFO:__main__:Importing data from payments.csv to payments table...
INFO:__main__:Done importing data into database.
```

* Run query

```
python sql-query/query.py
```

returns:
```
INFO:__main__:Query executed successfully
INFO:__main__:Query: 
Retrieve all users with date_joined of today, the number of contracts each user has, 
and the number of contracted cases (a case is contracted if it has at least one payment) 
using SQL Language.
INFO:__main__:Total rows returned: 2
INFO:__main__:Row 0: user_id=7, username=user7, total_contracts=1, contracted_cases=1
INFO:__main__:Row 1: user_id=10, username=user10, total_contracts=1, contracted_cases=1
```


2. Given the following tables, assuming that Django models that reflect this information have already been created.

user_table
```
id: integer
date_joined: Timestamp
username: Varchar
name: Varchar
first_name: Varchar
```

contracts_table
```
Id: Integer
start_date: Timestamp
product_id: Integer
user_id: Integer
```

recurrent_contracts_table
```
Id: Integer
contract_id: Integer
```


Using Django's ORM, retrieve contracts with a start_date in the year 2020 that are not in the recurrent_contracts table and have a "name" field containing the text "Jho".

3.  Considering the information from the previous exercise, if the database contained millions of records in all tables, what technological resources would you use to optimize data retrieval time? You do not need to implement, just describe in your own words.

4. Given the tables from the first exercise (Payments, Contracts, and User), define the endpoints (API URLs and protocol) that should be created for:

* Create a user
* Modify a user
* List users
* List a user's contracts
* Validate a payment