from pymongo import MongoClient
import time

mongo_client = MongoClient("mongodb://127.0.0.1:27017/")
db = mongo_client["soen363"]
company_collection = db["companyTable"] 

print("connected successfully")

def find_company_by_name(name):
    start_time = time.time()
    result = company_collection.find_one({"company_name": name})
    end_time = time.time()
    return result,end_time-start_time

if __name__ == "__main__":
    company = find_company_by_name("Salesforce Inc")
    print(company)
