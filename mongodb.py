import pymongo
import os
from bson.json_util import dumps 

class Mongodb:

    def __init__(self):
        self.mongodb = pymongo.MongoClient(os.getenv("CONSTRING"))
        
        self.userCol = self.mongodb["ToDo"]["User_profile"]
        self.frameCol = self.mongodb["ToDo"]["Frame_profile"]

    def get_all_data(self, col):
        return self.get_col(col).find()

    def json(self, str):
        return dumps(str, indent=2)

    def get_col(self, s):
        if s == "users":
            return self.userCol
        else:
            return self.frameCol