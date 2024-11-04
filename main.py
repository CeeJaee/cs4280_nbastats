import pymongo
from pymongo import MongoClient
from flask import Flask, render_template

app = Flask(__name__)

client = pymongo.MongoClient("mongodb+srv://carljudeduran:across381surfGROUND@cs4280nba.vubh3.mongodb.net/")

db = client.nbastats

collectionTeams = db.teams

@app.route('/')
def index():
    # Query to get Stephen Curry's information
    document = collectionTeams.find_one({"_id": "GSW_2022-2023"})
    
    curry_info = None
    if document and "players" in document:
        for player in document["players"][0]:  # Access the first list inside 'players'
            if player["Player"] == "Stephen Curry":
                curry_info = player
                break
    
    # Pass the data to the HTML template
    return render_template('index.html', player=curry_info)

@app.route('/player/<player_name>')
def player_stats(player_name):
    # Standardize the player name format if needed (e.g., converting to title case)
    player_name = player_name.replace('-', ' ').title()

    # Query the document with the given team and season
    document = collectionTeams.find_one({"_id": "GSW_2022-2023"})
    
    player_info = None
    if document and "players" in document:
        for player in document["players"][0]:  # Access the first list inside 'players'
            if player["Player"].lower() == player_name.lower():
                player_info = player
                break
    
    # Pass the data to the HTML template
    return render_template('player.html', player=player_info)

if __name__ == '__main__':
    app.run(debug=True)

"""
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

"""
# Save the coach's name as a variable
coach_name = document["Coach"] if document and "Coach" in document else None

# Print the coach's name (or handle the case if it's not found)
if coach_name:
    print("Coach:", coach_name)
else:
    print("Coach not found.")
"""