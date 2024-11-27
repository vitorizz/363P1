import psycopg2

def create_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="soen363"
    )
    return conn
