from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime, timedelta

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['ecommerce']  # Use or create database




def stock_prediction():
    three_months_ago = datetime.now() - timedelta(days=90)
    
    
    pipeline = [
        
        {
            "$match": {
                "order_date": {"$gte": three_months_ago},
                "status": {"$in": ["delivered", "shipped"]}
            }
        },
        
        {"$unwind": "$products"},
        {
            "$group": {
                "_id": "$products.product_id",
                "total_units_sold": {"$sum": "$products.quantity"},
                "days_sold": {"$addToSet": {"$dateToString": {"format": "%Y-%m-%d", "date": "$order_date"}}}
            }
        },
        
        {
            "$project": {
                "total_units_sold": 1,
                "unique_days": {"$size": "$days_sold"},
                "avg_units_per_day": {
                    "$cond": [
                        {"$gt": [{"$size": "$days_sold"}, 0]},
                        {"$divide": ["$total_units_sold", {"$size": "$days_sold"}]},
                        0
                    ]
                }
            }
        },
     
        {
            "$lookup": {
                "from": "products",
                "localField": "_id",
                "foreignField": "_id",
                "as": "product_details"
            }
        },

        {"$unwind": "$product_details"},

        {
            "$project": {
                "product_name": "$product_details.name",
                "current_stock": "$product_details.stock",
                "avg_units_per_day": 1,
                "projected_sales_next_month": {"$multiply": ["$avg_units_per_day", 30]},
                "projected_stock": {
                    "$cond": [
                        {"$gt": [{"$multiply": ["$avg_units_per_day", 30]}, "$product_details.stock"]},
                        0,
                        {"$subtract": ["$product_details.stock", {"$multiply": ["$avg_units_per_day", 30]}]}
                    ]
                }
            }
        }
    ]
    
    results = db.orders.aggregate(pipeline)
    
    print("Projected Stock Availability for Each Product Over the Next Month:")
    for product in results:
        print(f"Name: {product['product_name']}, Current Stock: {product['current_stock']}, "
              f"Projected Stock: {product['projected_stock']:.2f}")


stock_prediction()
