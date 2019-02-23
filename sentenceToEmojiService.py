from flask import Flask, request
from flask_restful import Api, Resource
import textAnalyzer

app = Flask(__name__)
api = Api(app)

class TextAnalyzer(Resource):
    def get(self, input_text):
        
        return {'answer': input_text}

api.add_resource(TextAnalyzer, '/analyze/<string:input_text>')

if __name__ == '__main__':
    app.run(debug=True)