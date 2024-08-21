#!/usr/bin/env python3
''' Module that provides some stats about Nginx logs stored in MongoDB '''
from pymongo import MongoClient

# Connect to MongoDB (make sure MongoDB is running on localhost:27017)
client = MongoClient('mongodb://localhost:27017/')

# Access the 'logs' database and 'nginx' collection
db = client.logs
collection = db.nginx

# Count the total number of documents in the collection
total_logs = collection.count_documents({})

# Count documents by HTTP methods
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
method_counts = {method: collection.count_documents({"method": method}) for method in methods}

# Count documents with method GET and path /status
status_check = collection.count_documents({"method": "GET", "path": "/status"})

# Print the results
print(f"{total_logs} logs")
print("Methods:")
for method in methods:
    print(f"\tmethod {method}: {method_counts[method]}")
print(f"{status_check} status check")
