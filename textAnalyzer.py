from textblob import TextBlob

def analyze_text(input_text):
    input_text_blob = TextBlob(input_text)
    #todo: error try catch
    language = input_text_blob.detect_language()
    if language != 'en':
        input_text_blob = input_text_blob.translate(from_lang=language, to='en')

    sentences = input_text_blob.sentences

    for sentence in sentences:
        print(sentence.sentiment)

if __name__ == '__main__':
    first_input = 'Eu sunt foarte fericit.'
    second_input = 'Babylon does a lot of great things!. I’m very happy that my team won the world cup!. I feel a bit sad today. The book is red. I am verry happy.'
    analyze_text(second_input)
    analyze_text(first_input)
    
#Use the correct() method to attempt spelling correction.
# nltk.download('punkt') -> for punctuation
# nltk needed to download punkt
