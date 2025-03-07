# import tornado.web
# import os
# import uuid
# from models.file import save_file, get_files

# class FileHandler(tornado.web.RequestHandler):
#     @tornado.web.authenticated
#     def get(self):
#         user = self.current_user
#         files = get_files()
#         self.render("files.html", user=user, files=files)

#     @tornado.web.authenticated
#     def post(self):
#         user = self.current_user
#         if not user["roles"].get("upload", False):
#             self.write("You do not have permission to upload files")
#             return

#         file = self.request.files['file'][0]
#         filename = file['filename']
#         file_id = str(uuid.uuid4())
#         filepath = os.path.join("uploads", file_id)

#         with open(filepath, 'wb') as f:
#             f.write(file['body'])

#         save_file(file_id, filename, user["username"])
#         self.redirect("/files")



import tornado.web
import os
import uuid
from models.file import save_file, get_files

class FileHandler(tornado.web.RequestHandler):
    @tornado.web.authenticated
    def get(self):
        user = self.current_user
        files = get_files()
        self.render("files.html", user=user.decode('utf-8'), files=files)

    @tornado.web.authenticated
    def post(self):
        user = self.current_user
        if not user:
            self.redirect("/login")
            return

        file = self.request.files['file'][0]
        filename = file['filename']
        file_id = str(uuid.uuid4())
        filepath = os.path.join("uploads", file_id)

        with open(filepath, 'wb') as f:
            f.write(file['body'])

        save_file(file_id, filename, user.decode('utf-8'))
        self.redirect("/files")