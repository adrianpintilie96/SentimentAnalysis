from flask import Flask, request
from flask_restful import Api, Resource
from textAnalyzer import analyze_sentence, polarity_to_category

app = Flask(__name__)
api = Api(app)

class TextAnalyzer(Resource):
    def get(self, input_text):
        polarity = analyze_sentence(input_text)
        category = polarity_to_category(polarity)
        #todo: use os.path?
        image_path = "/static/images/" + category + ".png"
        return {'category': image_path}

api.add_resource(TextAnalyzer, '/analyze/<string:input_text>')

#todo remove debig
if __name__ == '__main__':
    app.run(debug=True)