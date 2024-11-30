from pymongo import MongoClient
from datetime import datetime
import pandas as pd
import time

def top_entities(from_date='2024-11-01', to_date='2024-11-30'):
    mongo_client = MongoClient("mongodb://127.0.0.1:27017/")
    db = mongo_client["soen363"]

    financials_collection = db['StockPrice']

    from_date = datetime.strptime(from_date, '%Y-%m-%d')
    to_date = datetime.strptime(to_date, '%Y-%m-%d')
    pipeline = [
        {"$match": {"price_date":{"$gte":from_date, "$lte":to_date}}},
        {"$group": {"_id": "$company_id", "highest_price": {"$max": "$high_price"}}},
        {"$sort": {"highest_price": -1}},
        {"$limit": 10}
    ]
    start_time = time.time()
    agg = financials_collection.aggregate(pipeline)
    end_time = time.time()
    query_time = end_time - start_time
    
    # print(f"Lowest stock price for each company from '{from_date}' to '{to_date}' :")
    # for doc in agg:
    #     print(doc)
    # mongo_client.close()
    # print(f"Query time: {query_time}")
    return list(agg),query_time
     
if __name__ == "__main__":
    top_entities()