from flask import Flask
from flask import request
from pymongo import MongoClient
from dotenv import dotenv_values

app = Flask(__name__)

config = dotenv_values()

uri = f"mongodb+srv://jamesg:{config['MONGO_PWD']}@cluster0.xjm0dm7.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)


@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/chuck')
def chuck():
    name = request.args.get("name", "Chuck")

    database = client.get_database("sample_mflix")
    movies = database.get_collection("movies")
    # Query for a movie that has the title 'Back to the Future'
    query = { "title": "Back to the Future" }
    movie = movies.find_one(query)
    client.close()

    return f'Hello, {name}, {movie}!'
 

