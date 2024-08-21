#!/usr/bin/env python3
"""Python function that lists all documents in a collection"""
from pymongo import MongoClient


def list_all(mongo_collection):
    """
    List all documents in a collection.

    Parameters:
    mongo_collection (pymongo.collection.Collection):
    The pymongo collection object.

    Returns:
    list: A list of documents (dictionaries) from the collection.
    Returns an empty list if no documents are found.
    """
    return list(mongo_collection.find())
