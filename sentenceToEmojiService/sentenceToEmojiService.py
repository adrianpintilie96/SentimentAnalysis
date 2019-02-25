from flask import Flask, request
from flask_restful import Api, Resource
from resources.sentenceToEmoji import SentenceToEmoji

app = Flask(__name__)
api = Api(app)

api.add_resource(SentenceToEmoji, '/analyze/<string:input_text>')
