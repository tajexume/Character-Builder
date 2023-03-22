import os

from character_builder import FakeCharacter

import os
import json

from flask import Flask, request, jsonify

from flask_mysqldb import MySQL
from dotenv import load_dotenv

load_dotenv()

api = Flask(__name__)
sql = MySQL(api)

# MySQL Configurations
api.config["MYSQL_HOST"] = os.environ.get("MYSQL_HOST")
api.config["MYSQL_USER"] = os.environ.get("MYSQL_USER")
api.config["MYSQL_PASSWORD"] = os.environ.get("MYSQL_PASSWORD")
api.config["MYSQL_DB"] = os.environ.get("MYSQL_DB")
api.config["MYSQL_PORT"] = os.environ.get("MYSQL_PORT")


@api.route("/", methods=["GET"])
def main():
    cur = sql.connection.cursor()
    res = cur.execute("SELECT * FROM attributes")
    row = cur.fetchone()
    return f"{row[0], row[1], row[2]}", 200


@api.route("/get_character/<characterID>", methods=["GET"])
def get_character(characterID: int):
    cur = sql.connection.cursor()
    results = cur.execute("SELECT * FROM attributes where id=%s", (characterID,))
    if results > 0:
        row = cur.fetchone()
        character = FakeCharacter(characterID=row[0], dob=row[3], height=row[4],
                                  weight=row[5], race=row[6], creator=row[7])
        character.create_bio("Help")
    else:
        return "No Character was found with that information", 204

    return {"Attributes": character.jsonify()}, 200


if __name__ == "__main__":
    api.run(host="0.0.0.0", port=5000, debug=True)
