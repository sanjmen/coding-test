import csv
import logging

from settings import TABLES_INFO, CREATE_TABLES_SQL, DATA_DIR, SCRIPTS_DIR
from psql_cli import get_connection

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def drop_tables(cur):
    """drop tables in the database"""
    logger.info("Dropping tables in database...")
    for table_name, _, _ in TABLES_INFO:
        cur.execute(f"DROP TABLE IF EXISTS {table_name} CASCADE")


def create_tables(cur):
    """create tables in the PostgreSQL database"""
    logger.info("Creating tables in database...")
    file_path = SCRIPTS_DIR / CREATE_TABLES_SQL
    cur.execute(open(file_path, "r").read())


def import_data_to_tables(cur):
    """import data from csv files into tables"""
    logger.info("Importing data into tables...")
    for table_name, columns, csv_file in TABLES_INFO:
        logger.info(f"Importing data from {csv_file} to {table_name} table...")
        file_path = DATA_DIR / csv_file
        with open(file_path, "r") as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                cur.execute(
                    f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({', '.join(['%s'] * len(columns))})",
                    row,
                )


def main():
    logger.info("Starting data import process...")
    conn = get_connection()
    cur = conn.cursor()
    drop_tables(cur)
    create_tables(cur)
    import_data_to_tables(cur)
    conn.commit()
    cur.close()
    conn.close()
    logger.info("Done importing data into database.")


if __name__ == "__main__":
    main()
