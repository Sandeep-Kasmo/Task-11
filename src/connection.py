import pymongo
from pymongo import MongoClient

global client
client=None
def establish_connection():
    global client
    try:
        client=MongoClient("mongodb://localhost:27017/")
        print('Connection sucessful!')
        return client
    except Exception as e:
        print(f'Error connecting to MongoDB:{e}')
        return None

def close_connection():
    if client:
        client.close()
        print('Closed connection')
    