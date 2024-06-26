from pathlib import Path

DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASSWORD = "postgres"
DB_HOST = "localhost"
DB_PORT = "5432"

DATA_DIR = Path("data")
SCRIPTS_DIR = Path("scripts")
CREATE_TABLES_SQL = "create_tables.sql"
USERS_TABLE = "users"
CONTRACTS_TABLE = "contracts"
PAYMENTS_TABLE = "payments"

TABLES_INFO = (
    (USERS_TABLE, ["id", "date_joined", "username"], "users.csv"),
    (CONTRACTS_TABLE, ["id", "start_date", "product_id", "user_id"], "contracts.csv"),
    (PAYMENTS_TABLE, ["id", "payment_date", "contract_id", "amount"], "payments.csv"),
)
