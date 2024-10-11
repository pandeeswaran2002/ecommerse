from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime, timedelta


client = MongoClient('mongodb://localhost:27017/')
db = client['ecommerce']

def high_value_users(threshold=10000):
    pipeline = [
 
        {
            "$group": {
                "_id": "$user_id",
                "total_spent": {"$sum": "$total_amount"}
            }
        },
    
        {
            "$match": {
                "total_spent": {"$gt": threshold}
            }
        },

        {
            "$lookup": {
                "from": "users",
                "localField": "_id",
                "foreignField": "_id",
                "as": "user_details"
            }
        },

        {"$unwind": "$user_details"},

        {
            "$project": {
                "name": "$user_details.name",
                "email": "$user_details.email",
                "total_spent": 1
            }
        },

        {"$sort": {"total_spent": -1}}
    ]
    
    results = db.orders.aggregate(pipeline, allowDiskUse=True)
    
    print(f"Users who have spent more than ${threshold}:")
    for user in results:
        print(f"Name: {user['name']}, Email: {user['email']}, Total Spent: ${user['total_spent']}")


high_value_users()
