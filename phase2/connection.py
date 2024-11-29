import psycopg2
from dotenv import load_dotenv
import os

load_dotenv('./.env.local')
def create_connection():
    # print(f"""host={os.getenv("HOST")}\n
    #     database={os.getenv("DATABASE")}\n
    #     user={os.getenv("DB_USER")}\n
    #     password={os.getenv("PASSWORD")}\n
    #     port={os.getenv("PORT")}""")
    conn = psycopg2.connect(
        host=os.getenv("HOST"),
        database=os.getenv("DATABASE"), 
        user=os.getenv("DB_USER"),
        password=os.getenv("PASSWORD"),
    )
    # print(f"""host={os.getenv("HOST")}\n
    #     database={os.getenv("DATABASE")}\n
    #     user={os.getenv("USER")}\n
    #     password={os.getenv("PASSWORD")}\n
    #     port={os.getenv("PORT")}""")
    return conn

# create_connection()