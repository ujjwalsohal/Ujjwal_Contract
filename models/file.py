# from pymongo import MongoClient

# client = MongoClient("mongodb://localhost:27017/")
# db = client["file_management"]
# files_collection = db["files"]

# def save_file(file_id, filename, uploaded_by):
#     files_collection.insert_one({
#         "file_id": file_id,
#         "filename": filename,
#         "uploaded_by": uploaded_by
#     })

# def get_files():
#     return list(files_collection.find())



from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["file_management"]
files_collection = db["files"]

def save_file(file_id, filename, uploaded_by):
    files_collection.insert_one({
        "file_id": file_id,
        "filename": filename,
        "uploaded_by": uploaded_by
    })

def get_files():
    return list(files_collection.find())