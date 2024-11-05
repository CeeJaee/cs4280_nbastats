import pymongo
from pymongo import MongoClient
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

client = pymongo.MongoClient("mongodb+srv://carljudeduran:across381surfGROUND@cs4280nba.vubh3.mongodb.net/")

db = client.nbastats

collectionTeams = db.teams

# Main route to render the index page
@app.route('/')
def index():
    return render_template('index.html')

# Search route to process the player search and redirect
@app.route('/search', methods=['POST'])
def search():
    player_name = request.form.get('player_name')  # Retrieve the player name from the form
    # Convert spaces to hyphens for the URL, if necessary
    player_name_url = player_name.replace(' ', '-')
    return redirect(url_for('player_stats', player_name=player_name_url))

# player stats page
@app.route('/player/<player_name>')
def player_stats(player_name):
    # Standardize player name format (replace '-' with ' ' and capitalize words)
    player_name = player_name.replace('-', ' ').title()

    # Query the document with the specified team and season
    document = collectionTeams.find_one({
        "players": {
            "$elemMatch": {
                "Player": player_name
            }
        }
    })
    
    player_info = None
    # Verify that the document and 'players' list exist
    if document and "players" in document:
        # Loop through the list of players to find a match
        for player in document["players"]:
            if player["Player"].lower() == player_name.lower():
                player_info = player
                 # Retrieve games if they exist
                games = player.get("games", [])
                break
    
    # Pass player info to HTML template for display
    return render_template('player.html', player=player_info, games=games)

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