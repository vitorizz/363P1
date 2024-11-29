from pymongo import MongoClient
import time

def count_companies_by_country(country):
    mongo_client = MongoClient("mongodb://127.0.0.1:27017/")
    db = mongo_client["soen363"]
    company_collection = db["companyTable"]

    pipeline = [
        {"$match": {"country": country}}, 
        {"$group": {"_id": None, "count": {"$sum": 1}}}
    ]
    start_time = time.time()
    result = company_collection.aggregate(pipeline)
    end_time = time.time()
    result = list(result)  
    count = result[0]['count'] if result else 0 

    mongo_client.close()
    return count, end_time - start_time

# Example usage
country_name = "USA"
company_count = count_companies_by_country(country_name)
print(f"Number of companies from {country_name}: {company_count}")