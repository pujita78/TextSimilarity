from flask import Flask, request
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)

class PujiTest(Resource):
    def get(self):
        return "Hello Test "

api.add_resource(PujiTest, '/MyFirstAPITest')