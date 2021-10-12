from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast
import board

app = Flask(__name__)
api = Api(app)

class Users(Resource):
    def get(self):
        test = board.getBoard()
        return(test.PlayerList)

class Locations(Resource):
    # methods go here
    pass

api.add_resource(Users, '/users')  # '/users' is our entry point for Users
api.add_resource(Locations, '/locations')  # and '/locations' is our entry point for Locations

if __name__ == '__main__':
    app.run(port=4004)  # run our Flask app
