CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    date_joined TIMESTAMP NOT NULL,
    username VARCHAR(255) NOT NULL
);

CREATE TABLE contracts (
    id SERIAL PRIMARY KEY,
    start_date TIMESTAMP NOT NULL,
    product_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL
);

CREATE TABLE payments (
    id SERIAL PRIMARY KEY,
    payment_date TIMESTAMP NOT NULL,
    contract_id INTEGER NOT NULL,
    amount FLOAT NOT NULL,
    FOREIGN KEY (contract_id) REFERENCES contracts (id)
);