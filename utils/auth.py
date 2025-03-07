# # utils/auth.py
# import bcrypt

# def hash_password(password):
#     """
#     Hashes a password using bcrypt.
#     """
#     return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# def check_password(hashed_password, user_password):
#     """
#     Checks if the provided password matches the hashed password.
#     """
#     return bcrypt.checkpw(user_password.encode('utf-8'), hashed_password)




import bcrypt

def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def check_password(hashed_password, user_password):
    return bcrypt.checkpw(user_password.encode('utf-8'), hashed_password)