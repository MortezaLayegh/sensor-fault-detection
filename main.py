from sensor.configuration.mongo_db_connection import MongoDBClient

if __name__ == "__main__":
    client = MongoDBClient()
    print("collection name:",client.database.list_collection_names())