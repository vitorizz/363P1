from pymongo import MongoClient
import connection as conn
from bson import Decimal128
import datetime
import decimal

# Connect to PostgreSQL database
connection = conn.create_connection()
cursor = connection.cursor()


# MongoDB connection
mongo_client = MongoClient("mongodb://127.0.0.1:27017/")
mongo_db = mongo_client["soen363"]
CompanyFinancials_collection = mongo_db["CompanyFinancials"] 

try:

    cursor.execute("SELECT * FROM company_financials;") 
    company_rows = cursor.fetchall()


    cursor.execute("SELECT column_name FROM information_schema.columns WHERE table_name = 'company_financials';") 
    columns = [col[0] for col in cursor.fetchall()]
    print(columns)

    for row in company_rows:
        document = {}
        for i in range(len(columns)):
            value = row[i]
            if isinstance(value, decimal.Decimal):
                document[columns[i]] = Decimal128(str(value))
            elif isinstance(value, datetime.date):
                document[columns[i]] = datetime.datetime.combine(value, datetime.datetime.min.time())
            else:
                document[columns[i]] = value
                print(value)

        # print(document)
        CompanyFinancials_collection.insert_one(document) 

    print(f"Successfully migrated {len(company_rows)} rows from Company table to MongoDB.")

finally:
    # Close connections
    cursor.close()
    connection.close()
    mongo_client.close()