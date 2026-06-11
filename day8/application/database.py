from pymongo import MongoClient
import certifi

client=MongoClient("mongodb+srv://Yashwanth_C:yashu2005@yashwanth-c.ziy5pcf.mongodb.net/",
    tlsCaFile=certifi.where())

db=client["studentdb"]
students_collection=db["students"]
