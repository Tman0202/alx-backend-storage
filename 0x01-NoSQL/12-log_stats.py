#!/usr/bin/env python3
"""
Script that provides some stats about Nginx logs stored in MongoDB
Database: logs, Collection: nginx
first line: x logs, where x is the number of documents in this collection
second line: Methods:
5 lines with method = ["GET", "POST", "PUT", "PATCH", "DELETE"]
one line with method=GET, path=/status
"""
from pymongo import MongoClient


global METHODS

METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]


def log_stats_method(mongo_collection, method):
    """
    Prototype: def log_stats_method(mongo_collection, method):
    Provide some stats about some specific http methods in the log
    """
    value = mongo_collection.count_documents(
        {"method": {"$regex": method}}
    )
    print(f"\tmethod {method}: {value}")
    return
    
def log_stats(mongo_collection):
    """
    Prototype: def log_stats(mongo_collection, option=None):
    Provide some stats about Nginx logs stored in MongoDB
    """
    total = mongo_collection.count_documents({})
    print(f"{total} logs")
    print("Methods:")
    
    for method in METHODS:
        log_stats_method(nginx_collection, method)
    status_check = mongo_collection.count_documents({"path": "/status"})
    print(f"{status_check} status check")


if __name__ == "__main__":
    nginx_collection = MongoClient('mongodb://127.0.0.1:27017').logs.nginx
    log_stats(nginx_collection)
