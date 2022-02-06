#!/usr/bin/env python3

from flask import Flask, Response, jsonify, request
import json

KNIHY = [
    {"id": 0, "nazov": "Harry Potter 1", "popis": "Harry Potter a Kamen mudrcov"},
    {"id": 1, "nazov": "Harry Potter 2", "popis": "Harry Potter a Tajomna komnata"},
    {"id": 2, "nazov": "Python for Dummies", "popis": "Starting with Python"},
]

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Flaskovy index.</h1>"

@app.route("/knihy", methods=["GET"])
def dajKnihy():
    # vystup = ""
    # for kniha in KNIHY:
    #     vystup += "Nazov: {}, popis: {}\n".format(kniha["nazov"], kniha["popis"])
    # return vystup, 200
    return jsonify(KNIHY), 200

@app.route("/knihy/<int:paID>", methods=["GET"])
def dajKnihu(paID):
    for kniha in KNIHY:
        if kniha["id"] == paID:
            # return "Nazov: {}, popis: {}\n".format(kniha["nazov"], kniha["popis"]), 200
            # return Response(response=json.dumps(kniha), status=200, mimetype="application/json")
            return jsonify(kniha), 200
    return jsonify({"error": "Index neexistuje"}), 404

@app.route("/knihy", methods=["POST"])
def pridajKnihu():
    polozka = request.json
    lastID = 0
    for kniha in KNIHY:
        if kniha["id"] > lastID:
            lastID = kniha["id"]
    polozka["id"] = lastID+1

    KNIHY.append(polozka)

    return jsonify(polozka), 201

@app.route("/knihy/<int:paID>", methods=["DELETE"])
def vymazKnihu(paID):
    for kniha in KNIHY:
        if kniha["id"] == paID:
            KNIHY.remove(kniha)
            return jsonify(kniha), 200
    return jsonify({"error": "Index neexistuje"}), 404

if __name__ == "__main__":
    app.run("0.0.0.0", 8888)