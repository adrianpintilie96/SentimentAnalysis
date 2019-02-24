from flask import Flask, request
from flask_restful import Api, Resource
from textAnalyzer import TextAnalyzer

app = Flask(__name__)
api = Api(app)

class SentenceToEmoji(Resource):
    def get(self, input_text):
        textAnalyzer = TextAnalyzer(input_text)
        category = textAnalyzer.classify()
        image_path = "http://127.0.0.1:5000/static/images/" + category.name + ".png"
        return {'emoji': image_path}

api.add_resource(SentenceToEmoji, '/analyze/<string:input_text>')

#todo remove debug
if __name__ == '__main__':
    app.run(debug=True)