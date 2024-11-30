from pymongo import MongoClient
import time


def text_search(text="Netflix Kim Kardashian"):
    mongo_client = MongoClient("mongodb://127.0.0.1:27017/")
    db = mongo_client["soen363"]
    # company_collection = db["MarketNews"] 
    start_time = time.time()

    marketNews_collection = db.MarketNews

    marketNews_collection.create_index([
        ("title", "text"),
        ("headline", "text"),
        ("description", "text"),
        ("article_url", "text"),
    ])


    start_time = time.time()
    result = db.MarketNews.find({"$text": {"$search": text}})
    end_time = time.time()
    query_time = end_time - start_time
    
    
    
    return result, query_time

if __name__ == "__main__":
    result,query_time = list(text_search("Netflix Kim Kardashian"))
   
    print(result)
    print(f"Query time: {query_time}")

