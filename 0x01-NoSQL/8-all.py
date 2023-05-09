#!/usr/bin/env python3
""" 8 - list all """


def list_all(mongo_collection):
    """ 
    returns a list of all documents in the collection
    returns an empty list if there are no documents
    """
    if mongo_collection.find():
         return [doc for doc in mongo_collection.find()]
    return []
