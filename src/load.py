import pandas as pd
from pymongo import MongoClient
from pymongo.errors import PyMongoError

def load_to_mongo(df: pd.DataFrame, db_name: str, collection_name: str):
    try:
        client = MongoClient("mongodb://localhost:27017/")
        db = client[db_name]
        coll = db[collection_name]

        # drop old collection
        if collection_name in db.list_collection_names():
            db.drop_collection(collection_name)

        # convert dataframe -> list of dicts
        records = df.to_dict(orient="records")

        # insert into MongoDB
        if records:
            coll.insert_many(records)

        print(f"Inserted {len(records)} documents into {db_name}.{collection_name}")

        client.close()
        return True

    except PyMongoError as e:
        print(f"MongoDB Error: {e}")
        return False

    except Exception as e:
        print(f"Unexpected Error: {e}")
        return False
