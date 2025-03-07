# # handlers/admin.py
# import tornado.web
# from models.user import create_user, update_user_roles

# class AdminHandler(tornado.web.RequestHandler):
#     @tornado.web.authenticated
#     def get(self):
#         user = self.current_user
#         if not user["roles"].get("admin", False):
#             self.write("You do not have permission to access this page")
#             return

#         users = list(users_collection.find())
#         self.render("admin.html", user=user, users=users)

#     @tornado.web.authenticated
#     def post(self):
#         user = self.current_user
#         if not user["roles"].get("admin", False):
#             self.write("You do not have permission to perform this action")
#             return

#         action = self.get_body_argument("action")
#         if action == "create_user":
#             username = self.get_body_argument("username")
#             password = self.get_body_argument("password")
#             role = self.get_body_argument("role")

#             if users_collection.find_one({"username": username}):
#                 self.write("User already exists")
#                 return

#             create_user(username, password, role)
#             self.redirect("/admin")

#         elif action == "change_role":
#             username = self.get_body_argument("username")
#             role = self.get_body_argument("role")

#             update_user_roles(username, role)
#             self.redirect("/admin")




import tornado.web
from models.user import create_user, update_user_roles

class AdminHandler(tornado.web.RequestHandler):
    @tornado.web.authenticated
    def get(self):
        user = self.current_user
        if not user:
            self.redirect("/login")
            return

        users = list(users_collection.find())
        self.render("admin.html", user=user.decode('utf-8'), users=users)

    @tornado.web.authenticated
    def post(self):
        user = self.current_user
        if not user:
            self.redirect("/login")
            return

        action = self.get_body_argument("action")
        if action == "create_user":
            username = self.get_body_argument("username")
            password = self.get_body_argument("password")
            role = self.get_body_argument("role")

            if users_collection.find_one({"username": username}):
                self.write("User already exists")
                return

            create_user(username, password, role)
            self.redirect("/admin")

        elif action == "change_role":
            username = self.get_body_argument("username")
            role = self.get_body_argument("role")

            update_user_roles(username, role)
            self.redirect("/admin")