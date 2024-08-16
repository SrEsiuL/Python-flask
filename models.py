from pymongo import MongoClient
import certifi
from dotenv import dotenv_values

config = dotenv_values(".env")
MONGO_URI = config["DB_URL"]

ca = certifi.where()

def dbConnection():
    try:
        client = MongoClient(MONGO_URI, tlsCAFile=ca)
        db = client["CABJ"]

    except ConnectionError:
        print('Error de conexión con la db')
        
    return db
