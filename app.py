from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['your_database_name']
collection = db['your_collection_name']

@app.route('/')
def index():
    # Query to get Stephen Curry's information
    document = collection.find_one({"_id": "GSW_2022-2023"})
    
    curry_info = None
    if document and "players" in document:
        for player in document["players"][0]:  # Access the first list inside 'players'
            if player["Player"] == "Stephen Curry":
                curry_info = player
                break
    
    # Pass the data to the HTML template
    return render_template('index.html', player=curry_info)

if __name__ == '__main__':
    app.run(debug=True)