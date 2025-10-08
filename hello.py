from flask import Flask, request, jsonify
from pymongo import MongoClient
from dotenv import dotenv_values
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
cors = CORS(app, resources={
    r"/*":{
        "origins":"*"
    }
})

config = dotenv_values()

uri = f"mongodb+srv://jamesg:{config['MONGO_PWD']}@cluster0.xjm0dm7.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)


@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/chuck', methods=["POST","GET"])
def chuck():
    name = request.args.get("name", "Chuck")

    database = client.get_database("sample_mflix")
    movies = database.get_collection("movies")
    # Query for a movie that has the title 'Back to the Future'
    query = { "title": "Back to the Future" }
    movie = movies.find_one(query)

    return f'Hello, {name}, {movie}!'
 

@app.route('/post', methods=["POST"])
def postit():
    data = request.get_json()
    return jsonify(data)

@app.route('/getBestScore')
def getBestScore():
    result = client.myDB.scores.find_one({ 'name': 'James' })
    return result['bestScore']

@app.route('/setBestScore')
def setBestScore():
    bestScore = request.args.get("bestScore", 0)
    result = client.myDB.scores.update_one({'name':'James'}, { '$set': {'name': 'James', 'bestScore': bestScore } }, upsert=True)
    return jsonify({ 'matched_count': result.matched_count, 'modified_count': result.modified_count })

@app.route('/getGameState')
def getGameState():
    result = client.myDB.games.find_one({ 'name': 'James' })
    return jsonify(result["game_state"])


@app.route('/setGameState', methods=["POST"])
def setGameState():
    game_state = request.json
    result = client.myDB.games.update_one({'name':'James'}, { '$set': {'name': 'James', 'game_state': game_state } }, upsert=True)
    return str(result.inserted_id)

@app.route('/clearGameState')
def clearGameState():
    res = client.myDB.games.delete_many({ "name": "James" })
    return str(res.deleted_count)

