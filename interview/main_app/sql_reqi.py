import psycopg2
from psycopg2 import sql

def get_db_conn():
    return psycopg2.connect(
        host='localhost',
        port='1315',
        database='postgres',
        user='postgres',
        password='1337'
    )

def fetch_data_from_table(table_name):
    conn = get_db_conn()
    try:
        with conn.cursor() as cur:
            query = sql.SQL("SELECT * FROM {}").format(sql.Identifier(table_name))
            cur.execute(query)
            rows = cur.fetchall()
            return rows
    finally:
        conn.close()

def take_data_for_first_page():
    return fetch_data_from_table('text_for_first_page')

def take_data_for_second_page():
    return fetch_data_from_table('text_for_hidden_page')

def take_data_for_three_page():
    return fetch_data_from_table('block_for_hard_skills')

def take_data_for_four_page():
    return fetch_data_from_table('block_for_soft_skills')