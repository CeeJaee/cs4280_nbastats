import pymongo
from pymongo import MongoClient

# Set up the MongoDB client and access the database and collection
client = pymongo.MongoClient("mongodb+srv://carljudeduran:across381surfGROUND@cs4280nba.vubh3.mongodb.net/")

db = client.nbastats

collectionTeams = db.teams

# Query to retrieve Stephen Curry's information
document = collectionTeams.find_one(
    {"_id": "GSW_2022-2023"},
    {"players": {"$elemMatch": {"Player": "Stephen Curry"}}}
)

# Print the result
if document and "players" in document:
    stephen_curry = document["players"][0]  # Extract the first matching player
    print(stephen_curry)
else:
    print("Stephen Curry not found.")
