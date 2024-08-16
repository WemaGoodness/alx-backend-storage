#!/usr/bin/env python3
"""
Module to insert a document into a collection
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on kwargs.
    Args:
        mongo_collection: A pymongo collection object.
        **kwargs: The fields to insert in the new document.
    Returns:
        The _id of the new document.
    """
    return mongo_collection.insert_one(kwargs).inserted_id
