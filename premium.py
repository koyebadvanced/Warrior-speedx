# premium.py

def is_premium(user_id):
    try:
        with open("premium_users.txt", "r") as f:
            premium_ids = f.read().splitlines()
        return str(user_id) in premium_ids
    except:
        return False