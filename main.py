import pymongo
from pymongo import MongoClient

client = pymongo.MongoClient("mongodb+srv://carljudeduran:THXWings0731-@cs4280nba.vubh3.mongodb.net/")

db = client.nbastats

collectionTeams = db.teams

# Query to find the document by its `_id`
document = collectionTeams.find_one({"_id": "GSW_2022-2023"}, {"Coach": 1, "_id": 0})

# Query to find Stephen Curry's information
document = collectionTeams.find_one({"_id": "GSW_2022-2023"})

# Save Stephen Curry's details as a variable
curry_info = None
if document and "players" in document:
    for player in document["players"][0]:  # Access the first list inside 'players'
        if player["Player"] == "Stephen Curry":
            curry_info = player
            break

# Print Stephen Curry's information if found
if curry_info:
    print("Stephen Curry's info:", curry_info)
else:
    print("Stephen Curry not found.")

"""
# Save the coach's name as a variable
coach_name = document["Coach"] if document and "Coach" in document else None

# Print the coach's name (or handle the case if it's not found)
if coach_name:
    print("Coach:", coach_name)
else:
    print("Coach not found.")
"""