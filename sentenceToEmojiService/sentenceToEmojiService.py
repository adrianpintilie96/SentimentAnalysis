from flask import Flask, request
from flask_restful import Api, Resource
from resources import sentenceToEmojiRoute as route

app = Flask(__name__)
api = Api(app)

api.add_resource(route.SentenceToEmoji, '/analyze/<string:input_text>')

if __name__ == '__main__':
    app.run()
