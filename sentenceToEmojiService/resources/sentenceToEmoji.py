from flask_restful import Resource
from resources.sentimentAnalyzer import SentimentAnalyzer

class SentenceToEmoji(Resource):

    def get(self, input_text):
        """ Sentece to emoji route.
        get:
        summary: Endpoint responsible for returning an emoji that reflects
        the sentiment of the input text.
        parameters:
            - input_text: text to be classified
        returns:
            - 200:
                description: 
        """
        sentimentAnalyzer = SentimentAnalyzer(input_text)
        category = sentimentAnalyzer.classify()
        image_path = "http://127.0.0.1:5000/static/images/" + category.name + ".png"
        return {'emoji': image_path}