from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client.ecommerce

def customer_referral_chain(referral_code, depth=0):
    # Fetch user by referral code
    user = db.users.find_one({'referral_code': referral_code})
    
    if user:
        print(f"{'  ' * depth} - {user['name']} (Referral Code: {user['referral_code']})")
        # Find users who referred this user
        referrals = db.users.find({'referred_by': referral_code})
        for ref in referrals:
            customer_referral_chain(ref['referral_code'], depth + 1)

# Start the referral chain
customer_referral_chain("BOB456")
