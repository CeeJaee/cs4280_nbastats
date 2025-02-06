# cs4280_nbastats

need following libraries installed:
pip install pymongo
pip install flask
pip install flask-pymongo

# what is this project
this was a project that was migrated from my personal projects to a class I took from CSU Stanislaus.
The class was for CS4280 NOSQL databases. 

The following project is an NBA stats summary interface using a nosql database, mongodb.
The following tools and technologies were used:
- MongoDB
    - Database used
- MongoDB Atlas
    - Atlas is a database hosting service, used the free tier; there are paid subscriptions for larger storage
- MongoDB Compass
    - Compass is a database manipulation tool. Here, we can view databases and edit (add, remove, update) data entries
- VSCode
- GitHub
- Python, HTML, CSS

# challenges/learning curves
This would be the first time I developed a nosql database system with an accompanying GUI.

1. First, I needed to figure out how to set up the database to be able to be accessed online. This was where mongodb atlas comes in.
With atlas, I create my database cluster. Here, I created and named my database. Then, I created two collections named 'games' and 'teams'. From here, I could enter sample data temporarily for testing purposes. The schema of the data entries is shown below. Now that I have the database created and sample data entered, I needed the connection string for the database. This will allow for external programs to be able to connect to the DB, as well as being able to share the DB when needed. 
2. Once the database was set up, I needed to find a dataset that will allow me to perform queries for nba players, nba teams, and their respective stats. I originally browsed Kaggle, however, the data was not in the right format that I wanted (as in the organization of the data and what data was recorded as opposed to the type of file). I ended up using a website, basketballreference.com that provided csv file style data sheets for NBA players and teams for each season. Then, I converted the CSV file to JSON format using a converter. O