#!/usr/bin/python3
from models.base_model import BaseModel
# import json
# import os.path as path


a = BaseModel()
a.name = "Holberton"
a.save()

# if path.exists("file.json"):
#     with open("file.json") as file:
#         keys = ["name", "id", "__class__",
#                "my_number", "created_at", "updated_at"]
#         data = json.load(file)
#         lista = []
#         for key, value in data.items():
#             if key in keys:
#                 obj = BaseModel()
#                 setattr(obj, key, value)
#                 lista.append(obj)
#         print(lista)