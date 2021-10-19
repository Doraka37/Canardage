from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
import pandas as pd
import ast

app = Flask(__name__)
CORS(app)
api = Api(app)

class Users(Resource):
    def get(self):
        return("hello world")

class Connect(Resource):
    def post(self):
        print("voiozeiza")
        print("hello: ", request.form.get("username"))
        return("bravo tu es pd")

class Locations(Resource):
    # methods go here
    pass

api.add_resource(Users, '/users')  # '/users' is our entry point for Users
api.add_resource(Locations, '/locations')  # and '/locations' is our entry point for Locations
api.add_resource(Connect, '/connect')  # and '/locations' is our entry point for Locations

if __name__ == '__main__':
    app.run(port=4004)  # run our Flask app
