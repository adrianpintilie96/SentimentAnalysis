from textblob import TextBlob

def analyze_sentence(input_text):
    sentence = TextBlob(input_text)
    #todo: error try catch
    language = sentence.detect_language()
    if language != 'en':
        sentence = sentence.translate(from_lang=language, to='en')
    
    return sentence.polarity

def polarity_to_category(polarity):
    if polarity > 0.2:
        return "Happy"
    elif polarity < -0.2:
        return "Sad"
    else:
        return "Neutral"

if __name__ == '__main__':
    #todo: update the main
    first_input = 'Eu sunt foarte fericit.'
    second_input = 'Babylon does a lot of great things!. I’m very happy that my team won the world cup!. I feel a bit sad today. The book is red. I am verry happy.'
    analyze_text(second_input)
    analyze_text(first_input)
    
#Use the correct() method to attempt spelling correction.
# nltk.download('punkt') -> for punctuation
# nltk needed to download punkt
# why I choosed flask (elegance and simplicity, not familiar with python)


#process the data, validate the data 
#add to CV git, flask, rest
#authentification?
#support only sentences

'''Input Content: Sentences with less than three words cannot be analysed. This service supports up to 128KB of text (about 1000 sentences). A good use case would be tweets / Facebook posts of customers on company page.'''
"Content-type: Valid values are text/plain, text/html, or application/json.
"Input: It takes text input of at least two words."