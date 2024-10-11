from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime, timedelta
# Additional data for Orders Collection (recent orders)
client = MongoClient('mongodb://localhost:27017/')
db = client['ecommerce']

recent_orders = [
    { 
        "_id": ObjectId("64ff2f0e36d2953a7b8e87c4"), 
        "user_id": ObjectId("64ff2e0e36d2953a7b8e86b7"), 
        "order_date": datetime(2024, 7, 15), 
        "total_amount": 600, 
        "products": [ 
            { 
                "product_id": ObjectId("64ff30b036d2953a7b8e89b9"), 
                "quantity": 4, 
                "price_per_unit": 150 
            } 
        ], 
        "status": "cenceled" 
    },
    { 
        "_id": ObjectId("64ff2f0e36d2953a7b8e87c5"), 
        "user_id": ObjectId("64ff2e0e36d2953a7b8e86b8"), 
        "order_date": datetime(2024, 8, 20), 
        "total_amount": 1200, 
        "products": [ 
            { 
                "product_id": ObjectId("64ff30b036d2953a7b8e89c0"), 
                "quantity": 2, 
                "price_per_unit": 1000 
            } 
        ], 
        "status": "shipped" 
    },
    { 
        "_id": ObjectId("64ff2f0e36d2953a7b8e87c6"), 
        "user_id": ObjectId("64ff2e0e36d2953a7b8e86bb"), 
        "order_date": datetime(2024, 5, 10), 
        "total_amount": 500, 
        "products": [ 
            { 
                "product_id": ObjectId("64ff30b036d2953a7b8e89c1"), 
                "quantity": 2, 
                "price_per_unit": 250 
            } 
        ], 
        "status": "delivered" 
    },
    { 
        "_id": ObjectId("64ff2f0e36d2953a7b8e87c7"), 
        "user_id": ObjectId("64ff2e0e36d2953a7b8e86ba"), 
        "order_date": datetime(2024, 9, 5), 
        "total_amount": 800, 
        "products": [ 
            { 
                "product_id": ObjectId("64ff30b036d2953a7b8e89c2"), 
                "quantity": 1, 
                "price_per_unit": 800 
            } 
        ], 
        "status": "delivered" 
    },
    { 
        "_id": ObjectId("64ff2f0e36d2953a7b8e87c8"), 
        "user_id": ObjectId("64ff2e0e36d2953a7b8e86bc"), 
        "order_date": datetime(2024, 10, 1), 
        "total_amount": 900, 
        "products": [ 
            { 
                "product_id": ObjectId("64ff30b036d2953a7b8e89c3"), 
                "quantity": 3, 
                "price_per_unit": 300 
            } 
        ], 
        "status": "cenceled" 
    }
]

# Insert the recent orders into the Orders collection
db.orders.insert_many(recent_orders)

print("Recent orders inserted successfully!")
