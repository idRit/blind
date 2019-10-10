from flask import Flask, url_for, request, json, Response, jsonify
from flask_cors import CORS, cross_origin
from Blind import movies_func

from Blind import list_of_movies

app = Flask(__name__)
CORS(app)

@app.route("/", methods = ['GET'])
def index():

    note = {
        "success": True,
        "message": "working"
    }

    resp = jsonify(note)
    return resp


@app.route("/api/blindCheckMovie/<movie>", methods = ['GET'])
def blindCheck(movie):
    result = movies_func(movie)

    return jsonify({
        "success": True,
        "message": result
    })

@app.route('/api/getMovies/<team>', methods = ['GET'])
def getAllMovies(team):
    x = ""
    for i in range(0, len(list_of_movies)):
        if int(team) == i:
            x = list_of_movies[i]
    return jsonify({
        "success": True,
        "movie": x
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0")
