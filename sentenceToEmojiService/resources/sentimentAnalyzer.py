from textblob import TextBlob
from enum import Enum

emotion_categories = Enum('emotion_categories', 'happy neutral sad')

class SentimentAnalyzer:

    def __init__(self, input_text):
        self.sentence = TextBlob(input_text)

    def get_input_polarity(self):
        """Returns the polarity of the input text."""
        return self.sentence.polarity

    def translate_input_text(self):
        """
        Detects the language and translates the input text to english 
        using the Google Translate API.
        """
        language = self.sentence.detect_language()
        if language != 'en':
            self.sentence = self.sentence.translate(
                from_lang=language, to='en')

    def transform_polarity_to_category(self):
        """
        Transforms the polarity of the input text into a categorical value.
        Possible values of the enum: happy, neutral, sad.
        """
        polarity = self.get_input_polarity()
        if polarity > 0.2:
            self.category = emotion_categories.happy
        elif polarity < -0.2:
            self.category = emotion_categories.sad
        else:
            self.category = emotion_categories.neutral

    def classify(self):
        """
        Classifies the input text in one the possible categorical
        values: happy, neutral, sad.
        Also, it detects the language and translates the input text
        to english.
        """
        self.translate_input_text()
        self.transform_polarity_to_category()
        return self.category


if __name__ == '__main__':
    input_text = 'Babylon is great!'
    sentimentAnalyzer = SentimentAnalyzer(input_text)
    print(sentimentAnalyzer.classify().name)
 