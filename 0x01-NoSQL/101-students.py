#!/usr/bin/env python3
"""
Module to return all students sorted by average score
"""


def top_students(mongo_collection):
    """
    Returns all students sorted by average score.
    Args:
        mongo_collection: A pymongo collection object.
    Returns:
        A list of students with their average score sorted in descending order.
    """
    return list(mongo_collection.aggregate([
        {
            "$project": {
                "name": 1,
                "averageScore": { "$avg": "$topics.score" }
            }
        },
        { "$sort": { "averageScore": -1 } }
    ]))
