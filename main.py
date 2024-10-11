from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime, timedelta

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['ecommerce']  # Use or create database

# Data for Users Collection
users = [
    { "_id": ObjectId("64ff2e0e36d2953a7b8e86b7"), "name": "Alice", "email": "alice@example.com", "age": 29, "address": { "street": "Main St", "city": "New York", "zipcode": "10001", "country": "USA" }, "is_premium_member": True, "date_joined": datetime(2022, 8, 12), "referral_code": "ALICE123", "referred_by": "BOB456" },
    { "_id": ObjectId("64ff2e0e36d2953a7b8e86b8"), "name": "Bob", "email": "bob@example.com", "age": 35, "address": { "street": "Second St", "city": "Los Angeles", "zipcode": "90001", "country": "USA" }, "is_premium_member": False, "date_joined": datetime(2021, 5, 20), "referral_code": "BOB456", "referred_by": None },
    { "_id": ObjectId("64ff2e0e36d2953a7b8e86b9"), "name": "Charlie", "email": "charlie@example.com", "age": 42, "address": { "street": "Third St", "city": "Chicago", "zipcode": "60601", "country": "USA" }, "is_premium_member": True, "date_joined": datetime(2022, 10, 22), "referral_code": "CHARLIE789", "referred_by": "ALICE123" },
    { "_id": ObjectId("64ff2e0e36d2953a7b8e86ba"), "name": "Diana", "email": "diana@example.com", "age": 23, "address": { "street": "Fourth St", "city": "Houston", "zipcode": "77001", "country": "USA" }, "is_premium_member": False, "date_joined": datetime(2023, 1, 5), "referral_code": "DIANA987", "referred_by": "CHARLIE789" },
    { "_id": ObjectId("64ff2e0e36d2953a7b8e86bb"), "name": "Eve", "email": "eve@example.com", "age": 31, "address": { "street": "Fifth Ave", "city": "San Francisco", "zipcode": "94101", "country": "USA" }, "is_premium_member": True, "date_joined": datetime(2022, 7, 18), "referral_code": "EVE654", "referred_by": "ALICE123" },
    { "_id": ObjectId("64ff2e0e36d2953a7b8e86bc"), "name": "Frank", "email": "frank@example.com", "age": 39, "address": { "street": "Sixth St", "city": "Miami", "zipcode": "33101", "country": "USA" }, "is_premium_member": False, "date_joined": datetime(2020, 11, 11), "referral_code": "FRANK321", "referred_by": None }
]

# Data for Orders Collection
orders = [
    { "_id": ObjectId("64ff2f0e36d2953a7b8e87b8"), "user_id": ObjectId("64ff2e0e36d2953a7b8e86b7"), "order_date": datetime(2023, 1, 15), "total_amount": 350, "products": [ { "product_id": ObjectId("64ff30b036d2953a7b8e89b9"), "quantity": 2, "price_per_unit": 150 } ], "status": "cenceled" },
    { "_id": ObjectId("64ff2f0e36d2953a7b8e87b9"), "user_id": ObjectId("64ff2e0e36d2953a7b8e86b7"), "order_date": datetime(2023, 2, 12), "total_amount": 450, "products": [ { "product_id": ObjectId("64ff30b036d2953a7b8e89b9"), "quantity": 3, "price_per_unit": 150 } ], "status": "cenceled" },
    { "_id": ObjectId("64ff2f0e36d2953a7b8e87c0"), "user_id": ObjectId("64ff2e0e36d2953a7b8e86bb"), "order_date": datetime(2023, 3, 3), "total_amount": 12000, "products": [ { "product_id": ObjectId("64ff30b036d2953a7b8e89c0"), "quantity": 1, "price_per_unit": 500 } ], "status": "deliverd" },
    { "_id": ObjectId("64ff2f0e36d2953a7b8e87c1"), "user_id": ObjectId("64ff2e0e36d2953a7b8e86ba"), "order_date": datetime(2023, 4, 10), "total_amount": 250, "products": [ { "product_id": ObjectId("64ff30b036d2953a7b8e89b9"), "quantity": 1, "price_per_unit": 250 } ], "status": "canceled" },
    { "_id": ObjectId("64ff2f0e36d2953a7b8e87c2"), "user_id": ObjectId("64ff2e0e36d2953a7b8e86bb"), "order_date": datetime(2023, 2, 25), "total_amount": 750, "products": [ { "product_id": ObjectId("64ff30b036d2953a7b8e89c1"), "quantity": 3, "price_per_unit": 250 } ], "status": "delivered" },
    { "_id": ObjectId("64ff2f0e36d2953a7b8e87c3"), "user_id": ObjectId("64ff2e0e36d2953a7b8e86bc"), "order_date": datetime(2023, 6, 15), "total_amount": 400, "products": [ { "product_id": ObjectId("64ff30b036d2953a7b8e89c2"), "quantity": 2, "price_per_unit": 200 } ], "status": "canceled" }
]

# Data for Products Collection
products = [
    { "_id": ObjectId("64ff30b036d2953a7b8e89b9"), "name": "Smartphone", "category": "Electronics", "price": 500, "stock": 100, "rating": 4.5, "tags": ["phone", "gadget"], "discount": 10, "last_updated": datetime(2023, 3, 1) },
    { "_id": ObjectId("64ff30b036d2953a7b8e89c0"), "name": "Laptop", "category": "Electronics", "price": 1000, "stock": 50, "rating": 4.7, "tags": ["computer", "electronics"], "discount": 15, "last_updated": datetime(2023, 3, 15) },
    { "_id": ObjectId("64ff30b036d2953a7b8e89c1"), "name": "Headphones", "category": "Electronics", "price": 250, "stock": 200, "rating": 4.2, "tags": ["audio", "music"], "discount": 5, "last_updated": datetime(2023, 4, 10) },
    { "_id": ObjectId("64ff30b036d2953a7b8e89c2"), "name": "Camera", "category": "Electronics", "price": 800, "stock": 75, "rating": 4.6, "tags": ["photography", "camera"], "discount": 20, "last_updated": datetime(2023, 5, 20) },
    { "_id": ObjectId("64ff30b036d2953a7b8e89c3"), "name": "Smartwatch", "category": "Wearable", "price": 300, "stock": 150, "rating": 4.0, "tags": ["wearable", "gadget"], "discount": 12, "last_updated": datetime(2023, 6, 1) }
]

# Insert data into the respective collections
db.users.insert_many(users)
db.orders.insert_many(orders)
db.products.insert_many(products)

print("Data inserted successfully!")






