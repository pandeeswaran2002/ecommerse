from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime, timedelta

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['ecommerce']

def top_performing_products():
    six_months_ago = datetime.now() - timedelta(days=180)
    
    pipeline = [
     
        {
            "$match": {
                "order_date": {"$gte": six_months_ago},
                "status": {"$in": ["delivered", "shipped"]}
            }
        },
      
        {"$unwind": "$products"},
      
        {
            "$group": {
                "_id": "$products.product_id",
                "total_units_sold": {"$sum": "$products.quantity"},
                "total_revenue": {"$sum": {"$multiply": ["$products.quantity", "$products.price_per_unit"]}}
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
                "category": "$product_details.category",
                "total_units_sold": 1,
                "total_revenue": 1
            }
        },
 
        {"$sort": {"total_units_sold": -1}},
   
        {"$limit": 5}
    ]
    
    results = db.orders.aggregate(pipeline)
    
    print("Top 5 Performing Products in the Last 6 Months:")
    for product in results:
        print(f"Name: {product['product_name']}, Category: {product['category']}, "
              f"Units Sold: {product['total_units_sold']}, Revenue: ${product['total_revenue']}")


top_performing_products()

print(top_performing_products)
