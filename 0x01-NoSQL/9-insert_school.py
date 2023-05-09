#!/usr/bin/env python3
""" 9 - insert school """


def insert_school(mongo_collection, **kwargs):
    """ 
    inserts a new document in a collection based on kwargs:
    Returns the new _id
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
