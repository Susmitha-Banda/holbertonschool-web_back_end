#!/usr/bin/env python3
"""Python function that inserts a new document
in a collection based on kwargs"""
from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """
    Insert a new document in a collection with the given keyword arguments.

    Parameters:
    mongo_collection (pymongo.collection.Collection):
    The pymongo collection object.
    **kwargs: The fields and values to be inserted into the document.

    Returns:
    The _id of the newly inserted document.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
