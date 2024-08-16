#!/usr/bin/env python3
"""
Module to update topics of a school document
"""


def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a school document based on the name.
    Args:
        mongo_collection: A pymongo collection object.
        name (str): The school name to update.
        topics (list): The list of topics approached in the school.
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
