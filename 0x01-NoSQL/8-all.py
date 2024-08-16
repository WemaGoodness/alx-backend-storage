#!/usr/bin/env python3
"""
Module to list all documents in a collection
"""


def list_all(mongo_collection):
    """
    Lists all documents in a collection.
    Args:
        mongo_collection: A pymongo collection object.
    Returns:
        A list of documents, or an empty list if no documents found.
    """
    return list(mongo_collection.find())
