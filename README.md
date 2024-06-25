# coding-test

## Technical Backend Developer Test

1. Given the following SQL tables

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