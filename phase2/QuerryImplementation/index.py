from pymongo import MongoClient
import aggregateData as agg

def create_country_index():
    mongo_client = MongoClient("mongodb://127.0.0.1:27017/")
    db = mongo_client["soen363"]
    company_collection = db["companyTable"]

    # Create an index on the 'country' field
    company_collection.create_index([("country", 1)])

    mongo_client.close()

def aggredate_data_performance_test():
    country_name = "USA"
    mongo_client = MongoClient("mongodb://127.0.0.1:27017/")
    db = mongo_client["soen363"]
    company_collection = db["companyTable"]

    company_count, query_time_before = agg.count_companies_by_country(country_name)
    print("query time before index creation:", query_time_before)
    print(f"Number of companies from {country_name}: {company_count}")
    create_country_index()
    company_count, query_time_after = agg.count_companies_by_country(country_name)
    print("query time after index creation:", query_time_after)

    print(f"performance improvement: {((query_time_before - query_time_after)/query_time_before) * 100}%")
    company_collection.drop_index("country_1")

if __name__ == "__main__":
    aggredate_data_performance_test()
    