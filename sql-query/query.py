import logging

from psql_cli import get_connection

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

query_str = """
Retrieve all users with date_joined of today, the number of contracts each user has, 
and the number of contracted cases (a case is contracted if it has at least one payment) 
using SQL Language."""

query_sql = """
SELECT
    u.id AS user_id,
    u.username,
    COUNT(DISTINCT c.id) AS total_contracts,
    COUNT(DISTINCT p.contract_id) AS contracted_cases
FROM
    users u
LEFT JOIN
    contracts c ON u.id = c.user_id
LEFT JOIN
    payments p ON c.id = p.contract_id
WHERE
    u.date_joined = CURRENT_DATE
GROUP BY
    u.id, u.username;"""


def main():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(query_sql)
    rows = cur.fetchall()
    logger.info("Query executed successfully")
    logger.info("Query: %s", query_str)
    logger.info("Total rows returned: %s", len(rows))
    columns = [desc[0] for desc in cur.description]
    for n, row in enumerate(rows):
        r = [f"{column}={row[columns.index(column)]}" for column in columns]
        logger.info(f"Row {n}: {', '.join(r)}")


if __name__ == "__main__":
    main()
