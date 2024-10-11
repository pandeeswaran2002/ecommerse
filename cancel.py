from pymongo import MongoClient
from datetime import datetime, timedelta

client = MongoClient('mongodb://localhost:27017/')
db = client['ecommerce']

# Check the current date and time
print("Current system date and time:", datetime.now())

# Query to find all canceled orders
canceled_orders = db.orders.find({
    "status": "canceled"  # Removing the date constraint for testing
})

# Print the canceled orders
print("Canceled orders overall:")
for order in canceled_orders:
    print(order)


pipeline = [

    {
        "$group": {
            "_id": "$user_id",
            "canceled_orders_count": {"$sum": 1}
        }
    },

    {
        "$match": {
            "canceled_orders_count": {"$gt": 2}
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
            "_id": 0,
            "name": "$user_details.name",
            "email": "$user_details.email",
            "canceled_orders_count": 1
        }
    },
    
    {"$sort": {"canceled_orders_count": -1}}
]


results = db.orders.aggregate(pipeline)

print("Users with more than 2 canceled orders in total:")
for user in results:
    print(f"Name: {user['name']}, Email: {user['email']}, Canceled Orders: {user['canceled_orders_count']}")
