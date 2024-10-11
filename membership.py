from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime, timedelta

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['ecommerce']  # Use or create database


def premium_member_retention():
    one_year_ago = datetime.now() - timedelta(days=365)
    three_months_ago = datetime.now() - timedelta(days=90)
    
    
    pipeline = [
        
        {
            "$match": {
                "is_premium_member": True,
                "date_joined": {"$lte": one_year_ago}
            }
        },
        
        {
            "$lookup": {
                "from": "orders",
                "localField": "_id",
                "foreignField": "user_id",
                "as": "recent_orders",
                "pipeline": [
                    {"$match": {"order_date": {"$gte": three_months_ago}}}
                ]
            }
        },
        
        {
            "$addFields": {
                "has_recent_order": {"$gt": [{"$size": "$recent_orders"}, 0]}
            }
        },
        
        {
            "$group": {
                "_id": None,
                "total_premium_members": {"$sum": 1},
                "retained_members": {
                    "$push": {
                        "name": "$name",
                        "email": "$email"
                    }
                },
                "retained_count": {"$sum": {"$cond": ["$has_recent_order", 1, 0]}}
            }
        },
    
        {
            "$project": {
                "_id": 0,
                "percentage_retained": {
                    "$cond": [
                        {"$eq": ["$total_premium_members", 0]},
                        0,
                        {"$multiply": [{"$divide": ["$retained_count", "$total_premium_members"]}, 100]}
                    ]
                },
                "retained_members": "$retained_members"
            }
        }
    ]
    
    results = db.users.aggregate(pipeline)
    
    for result in results:
        percentage = result['percentage_retained']
        retained = [member['name'] for member in result['retained_members']]
        print(f"Percentage of premium members retained: {percentage:.2f}%")
        print("List of retained premium members:")
        for name in retained:
            print(f"- {name}")

# Execute the function
premium_member_retention()
