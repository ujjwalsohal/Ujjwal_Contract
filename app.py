# # # # import tornado.ioloop
# # # # import tornado.web
# # # # from handlers.auth import LoginHandler, LogoutHandler
# # # # from handlers.file import FileHandler
# # # # from handlers.admin import AdminHandler
# # # # from handlers.base import BaseHandler

# # # # def make_app():
# # # #     return tornado.web.Application([
# # # #         (r"/", MainHandler),
# # # #         (r"/login", LoginHandler),
# # # #         (r"/logout", LogoutHandler),
# # # #         (r"/files", FileHandler),
# # # #         (r"/admin", AdminHandler),
# # # #         (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": "static"}),
# # # #     ], cookie_secret="your_cookie_secret_here", login_url="/login")

# # # # if __name__ == "__main__":
# # # #     app = make_app()
# # # #     app.listen(8888)
# # # #     print("Server started at http://localhost:8888")
# # # #     tornado.ioloop.IOLoop.current().start()

# # # # app.py
# # # import tornado.ioloop
# # # import tornado.web
# # # from handlers.auth import LoginHandler, LogoutHandler
# # # from handlers.file import FileHandler
# # # from handlers.admin import AdminHandler

# # # def make_app():
# # #     return tornado.web.Application([
# # #         (r"/", MainHandler),
# # #         (r"/login", LoginHandler),
# # #         (r"/logout", LogoutHandler),
# # #         (r"/files", FileHandler),
# # #         (r"/admin", AdminHandler),
# # #         (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": "static"}),
# # #     ], cookie_secret="your_cookie_secret_here", login_url="/login")

# # # if __name__ == "__main__":
# # #     app = make_app()
# # #     app.listen(8888)
# # #     print("Server started at http://localhost:8888")
# # #     tornado.ioloop.IOLoop.current().start()

# # # app.py
# # import tornado.ioloop
# # import tornado.web
# # from handlers.auth import LoginHandler, LogoutHandler
# # from handlers.file import FileHandler
# # from handlers.admin import AdminHandler  # Correct import

# # def make_app():
# #     return tornado.web.Application([
# #         (r"/", MainHandler),
# #         (r"/login", LoginHandler),
# #         (r"/logout", LogoutHandler),
# #         (r"/files", FileHandler),
# #         (r"/admin", AdminHandler),
# #         (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": "static"}),
# #     ], cookie_secret="your_cookie_secret_here", login_url="/login")

# # if __name__ == "__main__":
# #     app = make_app()
# #     app.listen(8888)
# #     print("Server started at http://localhost:8888")
# #     tornado.ioloop.IOLoop.current().start()

# # app.py
# import tornado.ioloop
# import tornado.web
# from handlers.auth import LoginHandler, LogoutHandler
# from handlers.file import FileHandler
# from handlers.admin import AdminHandler
# from handlers.base import MainHandler  # Import MainHandler

# def make_app():
#     return tornado.web.Application([
#         (r"/", MainHandler),  # Add MainHandler route
#         (r"/login", LoginHandler),
#         (r"/logout", LogoutHandler),
#         (r"/files", FileHandler),
#         (r"/admin", AdminHandler),
#         (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": "static"}),
#     ], cookie_secret="your_cookie_secret_here", login_url="/login")

# if __name__ == "__main__":
#     app = make_app()
#     app.listen(8888)
#     print("Server started at http://localhost:8888")
#     tornado.ioloop.IOLoop.current().start()





import tornado.ioloop
import tornado.web
from handlers.auth import LoginHandler, LogoutHandler
from handlers.file import FileHandler
from handlers.admin import AdminHandler
from handlers.base import MainHandler



from models.user import create_user

# Create an initial admin user
create_user("admin", "admin123", {
    "view": True,
    "upload": True,
    "modify": True,
    "admin": True
})

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/login", LoginHandler),
        (r"/logout", LogoutHandler),
        (r"/files", FileHandler),
        (r"/admin", AdminHandler),
        (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": "static"}),
    ], 
    template_path="templates",  # Path to templates directory
    cookie_secret="your_cookie_secret_here",  # Replace with a secure secret
    login_url="/login")

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print("Server started at http://localhost:8888")
    tornado.ioloop.IOLoop.current().start()