# # import tornado.web
# # from models.user import find_user, check_password
# # from utils.auth import hash_password

# # class LoginHandler(tornado.web.RequestHandler):
# #     def get(self):
# #         self.render("login.html")

# #     def post(self):
# #         username = self.get_body_argument("username")
# #         password = self.get_body_argument("password")
# #         user = find_user(username)

# #         if user and check_password(user["password"], password):
# #             self.set_secure_cookie("user", username)
# #             self.redirect("/")
# #         else:
# #             self.write("Invalid username or password")

# # class LogoutHandler(tornado.web.RequestHandler):
# #     def get(self):
# #         self.clear_cookie("user")
# #         self.redirect("/login")

# # handlers/auth.py
# import tornado.web
# from models.user import find_user
# from utils.auth import hash_password, check_password  # Correct import

# class LoginHandler(tornado.web.RequestHandler):
#     def get(self):
#         self.render("login.html")

#     def post(self):
#         username = self.get_body_argument("username")
#         password = self.get_body_argument("password")
#         user = find_user(username)

#         if user and check_password(user["password"], password):
#             self.set_secure_cookie("user", username)
#             self.redirect("/")
#         else:
#             self.write("Invalid username or password")

# class LogoutHandler(tornado.web.RequestHandler):
#     def get(self):
#         self.clear_cookie("user")
#         self.redirect("/login")


import tornado.web
from models.user import find_user
from utils.auth import check_password

class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("login.html")

    def post(self):
        username = self.get_body_argument("username")
        password = self.get_body_argument("password")
        user = find_user(username)

        if user and check_password(user["password"], password):
            self.set_secure_cookie("user", username)
            self.redirect("/")
        else:
            self.write("Invalid username or password")

class LogoutHandler(tornado.web.RequestHandler):
    def get(self):
        self.clear_cookie("user")
        self.redirect("/login")