from pymongo import MongoClient

mongo_client = MongoClient("mongodb://127.0.0.1:27017/")
db = mongo_client["soen363"]
company_collection = db["companyTable"] 

print("connected successfully")

def find_company_by_name(name):
    result = company_collection.find_one({"company_name": name})
    return result

company = find_company_by_name("Salesforce Inc")
print(company)
