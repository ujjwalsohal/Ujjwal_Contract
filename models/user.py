# # # from pymongo import MongoClient
# # # import bcrypt

# # # client = MongoClient("mongodb://localhost:27017/")
# # # db = client["file_management"]
# # # users_collection = db["users"]

# # # def find_user(username):
# # #     return users_collection.find_one({"username": username})

# # # def create_user(username, password, roles):
# # #     hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
# # #     users_collection.insert_one({
# # #         "username": username,
# # #         "password": hashed_password,
# # #         "roles": roles
# # #     })

# # # def check_password(hashed_password, user_password):
# # #     return bcrypt.checkpw(user_password.encode('utf-8'), hashed_password)

# # # models/user.py
# # from pymongo import MongoClient
# # from utils.auth import hash_password, check_password  # Correct import

# # client = MongoClient("mongodb://localhost:27017/")
# # db = client["file_management"]
# # users_collection = db["users"]

# # def find_user(username):
# #     return users_collection.find_one({"username": username})

# # def create_user(username, password, roles):
# #     hashed_password = hash_password(password)  # Use the hash_password function
# #     users_collection.insert_one({
# #         "username": username,
# #         "password": hashed_password,
# #         "roles": roles
# #     })

# # models/user.py
# from pymongo import MongoClient
# from utils.auth import hash_password, check_password

# client = MongoClient("mongodb://localhost:27017/")
# db = client["file_management"]
# users_collection = db["users"]

# def find_user(username):
#     return users_collection.find_one({"username": username})

# def create_user(username, password, roles):
#     hashed_password = hash_password(password)
#     users_collection.insert_one({
#         "username": username,
#         "password": hashed_password,
#         "roles": roles
#     })

# def update_user_roles(username, role):
#     users_collection.update_one(
#         {"username": username},
#         {"$set": {"roles": role}}
#     )



from pymongo import MongoClient
from utils.auth import hash_password

client = MongoClient("mongodb://localhost:27017/")
db = client["file_management"]
users_collection = db["users"]

def find_user(username):
    return users_collection.find_one({"username": username})

def create_user(username, password, roles):
    hashed_password = hash_password(password)
    users_collection.insert_one({
        "username": username,
        "password": hashed_password,
        "roles": roles
    })

def update_user_roles(username, role):
    users_collection.update_one(
        {"username": username},
        {"$set": {"roles": role}}
    )