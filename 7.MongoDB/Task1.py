from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
uri = os.getenv("MONGODB_URI")
client = MongoClient(uri)
db = client["db1"]
collection = db["task1"]

document = {
    "name": "Purvi",
    "city": "Manawar"
}
insert_doc = collection.insert_one(document)
print("connected successfully")
client.close()