import pymongo
import pandas as pd
from pymongo import MongoClient
from bson.objectid import ObjectId #type:ignore
from connection import *



def get_data(database,collection,query={}):
    global client
    if client is None:
        client=establish_connection()
    
    db=client[database]
    coll=db[collection]

    try:
        data=list(coll.find(query))

        if not data:
            print('No data found')
            return pd.dataframe()
        
        for d in data:
            if '_id' in d:
                d['_id']=str(d['_id'])
        dataframe=pd.DataFrame(data)
        return dataframe
    except Exception as e:
        print(f'Error reading collection {collection}:{e}')
        return None
    


    