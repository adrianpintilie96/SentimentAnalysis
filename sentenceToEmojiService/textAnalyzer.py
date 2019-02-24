from textblob import TextBlob
from enum import Enum

emotion_categories = Enum('emotion_categories', 'happy neutral sad')

class TextAnalyzer:

    def __init__(self, input_text):
        self.sentence = TextBlob(input_text)

    def get_input_polarity(self):
        return self.sentence.polarity

    def translate_input_text(self):
        # todo: error try catch
        language = self.sentence.detect_language()
        if language != 'en':
            self.sentence = self.sentence.translate(from_lang=language, to='en')

    def transform_polarity_to_category(self):
        polarity = self.get_input_polarity()
        if polarity > 0.2:
            self.category = emotion_categories.happy
        elif polarity < -0.2:
            self.category = emotion_categories.sad
        else:
            self.category = emotion_categories.neutral

    def classify(self):
        self.translate_input_text()
        self.transform_polarity_to_category()
        return self.category

if __name__ == '__main__':
    input_text = 'Babylon does a lot of great things!.'
    textAnalyzer = TextAnalyzer(input_text)
    print(textAnalyzer.classify())
    


# todo: make this a class?

# Use the correct() method to attempt spelling correction.
# nltk.download('punkt') -> for punctuation
# nltk needed to download punkt
# why I choosed flask (elegance and simplicity, not familiar with python)


# process the data, validate the data
# add to CV git, flask, rest
# authentification?
# support only sentences

#'''Input Content: Sentences with less than three words cannot be analysed. This service supports up to 128KB of text (about 1000 sentences). A good use case would be tweets / Facebook posts of customers on company page.'''
#"Content-type: Valid values are text/plain, text/html, or application/json.
#"Input: It takes text input of at least two words."
