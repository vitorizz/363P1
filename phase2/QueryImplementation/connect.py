from pymongo import MongoClient 

def connect_mongo_client():
    mongo_client = MongoClient("mongodb://127.0.0.1:27017/")
    db = mongo_client["soen363"]
    return mongo_client,db