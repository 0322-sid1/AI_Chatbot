from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["chatbot_db"]
collection = db["conversations"]


def save_message(user_id, message, response):
    collection.insert_one({
        "user_id": user_id,
        "message": message,
        "response": response
    })


def get_last_intent(user_id):
    last = collection.find_one({"user_id": user_id}, sort=[("_id", -1)])
    if last:
        return last.get("intent")
    return None