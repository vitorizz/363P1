from pymongo import MongoClient
import aggregateData as agg
from connect import connect_mongo_client
import BasicQuerySearch as basic
import groupBy as group
import topEntities as top   

def create_country_index():
    mongo_client,db = connect_mongo_client()
    company_collection = db["companyTable"]

    # Create an index on the 'country' field
    company_collection.create_index([("country", 1)])

    mongo_client.close()

def aggredate_data_performance_test():
    country_name = "USA"
    mongo_client,db = connect_mongo_client()
    company_collection = db["companyTable"]

    company_count, query_time_before = agg.count_companies_by_country(country_name)


    company_collection.create_index([("country", 1)])
    company_count, query_time_after = agg.count_companies_by_country(country_name)
    
    print(f"Number of companies from {country_name}: {company_count}")
    print("query time before index creation:", query_time_before)
    print("query time after index creation:", query_time_after)

    print(f"performance improvement: {((query_time_before - query_time_after)/query_time_before) * 100}%")
    company_collection.drop_index("country_1")

def groupBy_index_performance_test():
    mongo_client,db = connect_mongo_client()
    stock_price = db["StockPrice"]

    agg, before_index_time = group.groupBy()

    stock_price.create_index([("price_date", 1)])


    agg, after_index_time = group.groupBy()

    print("before index time:", before_index_time)
    print("after index time:", after_index_time)
    print(f"performance improvement: {((before_index_time - after_index_time)/before_index_time) * 100}%")
    stock_price.drop_index("price_date_1")
    mongo_client.close()

def basic_query_performance_test():
    mongo_client,db = connect_mongo_client()
    company_collection = db["companyTable"]
    company, before_index_time= basic.find_company_by_name("Salesforce Inc")
    company_collection.create_index([("company_name", 1)])
    company, after_index_time = basic.find_company_by_name("Salesforce Inc")
    print(f"performance improvement: {((before_index_time - after_index_time)/before_index_time) * 100}%")
    
    company_collection.drop_index("company_name_1")
    mongo_client.close()

def topEntities_performance_test():
    mongo_client,db = connect_mongo_client()
    stockPriceCollection = db["StockPrice"]
    res, before_index_time = top.top_entities()
    stockPriceCollection.create_index([("price_date", 1), ("high_price", -1)])
    res, after_index_time = top.top_entities()
    print("before index time:", before_index_time)
    print("after index time:", after_index_time)
    print(f"performance improvement: {((before_index_time - after_index_time)/before_index_time) * 100}%")
    # stockPriceCollection.drop_index("price_date_1")
    # stockPriceCollection.drop_index("high_price_1")
    stockPriceCollection.drop_index("price_date_1_high_price_-1")
    mongo_client.close()


if __name__ == "__main__":
    print("Basic query performance test")
    basic_query_performance_test()
    print()

    print("Aggredate data performance test")
    aggredate_data_performance_test()
    print()

    print("Top entities performance test")
    topEntities_performance_test()
    print()

    print("Group by performance test")
    groupBy_index_performance_test()



    
    