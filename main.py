# This is a sample Python script.

from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
from controllers.studentController import StudentController
import pymongo
import certifi


app = Flask(__name__)
cors = CORS(app)
student_controller = StudentController()


@app.route("/", methods=["GET"])
def test():
    response = {
        "message": "hello world",
        "errors": []
    }
    return jsonify(response)


@app.route("/Bryan", methods=["GET"])
def get_data():
    response = {
        "name": "Gregorio",
        "years": 25,
        "casa": "cra ts dr tew"
    }
    return response


@app.route("/students", methods=["GET"])
def get_students():
    response = student_controller.index()
    return jsonify(response)


@app.route("/student/<id>", methods=["GET"])
def get_student(id):
    response = student_controller.show(id)
    return jsonify(response)


@app.route("/student", methods=["POST"])
def create_student():
    data = request.get_json()
    response = student_controller.create(data)
    return jsonify(response)


@app.route("/student/<id>", methods=["PUT"])
def update_student(id):
    data = request.get_json()
    response = student_controller.update(id, data)
    return jsonify(response)


@app.route("/student/<id>", methods=["DELETE"])
def delete_student(id):
    response = student_controller.delete(id)
    return jsonify(response)


def load_file_config():
    with open("config.json") as env:
        data = json.load(env)
    return data


if __name__ == '__main__':
    dataConfig = load_file_config()
    url = "http://" + dataConfig["url-backend"]+":"+str(dataConfig["port"])
    print("Server running", url)
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])
