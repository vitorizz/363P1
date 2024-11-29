from pymongo import MongoClient
import time

def top_entities():
    # Connect to MongoDB

    # Connect to MongoDB
    mongo_client = MongoClient("mongodb://127.0.0.1:27017/")
    db = mongo_client["soen363"]

    # Collections
    company_collection = db['companyTable']
    stock_price_collection = db['StockPrice']

    start_time1 = time.time()
    usa_companies = company_collection.find({"country": "USA"})
    end_time1 = time.time()
    query_time1 = end_time1 - start_time1

    usa_company_ids = [company['company_id'] for company in usa_companies]
    start_time2 = time.time()
    latest_prices = stock_price_collection.aggregate([
        {"$match": {"company_id": {"$in": usa_company_ids}}},
        {"$sort": {"price_date": -1}},
        {"$group": {
            "_id": "$company_id",
            "latest_close_price": {"$first": "$close_price"}
        }},
        {"$sort": {"latest_close_price": -1}},
        {"$limit": 10}
    ])
    end_time2 = time.time()
    query_time2 = end_time2 - start_time2

    print(f"Query time: {query_time1+query_time2}")
    top_companies = []
    for price in latest_prices:
        company = company_collection.find_one({"company_id": price["_id"]})
        if company:
            top_companies.append({
                "company_name": company["company_name"],
                "ticker_symbol": company["ticker_symbol"],
                "latest_close_price": price["latest_close_price"]
            })

    # Print out the results
    for idx, company in enumerate(top_companies, start=1):
        print(f"{idx}. {company['company_name']} ({company['ticker_symbol']}): ${company['latest_close_price']}")

    mongo_client.close()