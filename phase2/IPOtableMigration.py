import psycopg2
from pymongo import MongoClient
import connection as conn
from bson import Decimal128
import datetime
import decimal

# connect to postgres db
connection = conn.create_connection()
cursor = connection.cursor()

#mongo  connection
mongo_client = MongoClient("mongodb://127.0.0.1:27017/")
mongo_db = mongo_client["soen363"]
ipo_collection = mongo_db["ipo"]

try:
    #get data from postgres
    cursor.execute("SELECT * FROM ipo;")
    ipo_rows = cursor.fetchall()

    cursor.execute("SELECT column_name FROM information_schema.columns WHERE table_name = 'ipo';")
    columns = [col[0] for col in cursor.fetchall()]

    for row in ipo_rows:
        document = {}
        for i in range(len(columns)):
            value = row[i]
            if isinstance(value, decimal.Decimal):
                # decimal.Decimal to bson.Decimal128 conversion, bson expects certain type of values
                document[columns[i]] = Decimal128(str(value))
            elif isinstance(value, datetime.date):
                # use datetime.datetime to convert object
                document[columns[i]] = datetime.datetime.combine(value, datetime.datetime.min.time())
            else:
                document[columns[i]] = value

        ipo_collection.insert_one(document) 

    print(f"Successfully migrated {len(ipo_rows)} rows from IPO table to MongoDB.")

finally:
    # Close connections
    cursor.close()
    connection.close()
    mongo_client.close()