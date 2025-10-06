from flask import Flask, request, jsonify
from flask import request
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
    #data = {
    #        'chuck': 'walla',
    #        'foo': 'gila monster'
    #        }
    data = request.get_json()
    return jsonify(data)

@app.route('/getBestScore')
def getBestScore():
    return jsonify(666)

@app.route('/setBestScore')
def setBestScore():
    bestScore = request.args.get("bestScore", 0)

@app.route('/getGameState')
def getGameState():
    data = {
        "grid": {
            "size": 4,
            "cells": [
                [
                    None,
                    {
                        "position": {
                            "x": 0,
                            "y": 1
                        },
                        "value": 2
                    },
                    None,
                    None
                ],
                [
                    None,
                    None,
                    None,
                    None
                ],
                [
                    None,
                    None,
                    None,
                    None
                ],
                [
                    None,
                    {
                        "position": {
                            "x": 3,
                            "y": 1
                        },
                        "value": 2
                    },
                    None,
                    {
                        "position": {
                            "x": 3,
                            "y": 3
                        },
                        "value": 4
                    }
                ]
            ]
        },
        "score": 4,
        "over": False,
        "won": False,
        "keepPlaying": False
    }
    return jsonify(data)


@app.route('/setGameState', methods=["POST"])
def setGameState():
    game_state = request.json
    return jsonify({"game_state":"foopa"});
    # Content-Type was not 'application/json'.

@app.route('/clearGameState')
def clearGameState():
    return 'foo';

