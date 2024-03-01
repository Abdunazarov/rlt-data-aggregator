from pymongo import MongoClient

from settings import COLLECTION_NAME, DB_NAME, EXAMPLE_DATA, MONGODB_URI


def initialize_db():
    client = MongoClient(MONGODB_URI)
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]

    if collection.count_documents({}) == 0:
        collection.insert_many(EXAMPLE_DATA)
        print("DB initialized successfully")
    else:
        print("DB is already initialized")

if __name__ == "__main__":
    initialize_db()
