# # handlers/base.py
# import tornado.web

# class BaseHandler(tornado.web.RequestHandler):
#     def get_current_user(self):
#         return self.get_secure_cookie("user")

# class MainHandler(BaseHandler):
#     @tornado.web.authenticated
#     def get(self):
#         user = self.current_user
#         self.render("index.html", user=user)




import tornado.web

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("user")

class MainHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        user = self.current_user
        self.render("index.html", user=user.decode('utf-8'))