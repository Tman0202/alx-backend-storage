#!/usr/bin/env python3
""" 11-schools_by_topic """


def schools_by_topic(mongo_collection, topic):
    """ 
    returns the list of school having a specific topic:
    topic (string) will be the topic searched
    """
    return [school for school in mongo_collection.find( {"topics": topic} )]
