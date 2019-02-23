from textblob import TextBlob

text1 = 'Eu sunt fericit.'
text2 = 'The book is red. I am verry happy.'

input_text = TextBlob(text1)
#todo: error try catch
language = input_text.detect_language()
translated = input_text.translate(from_lang=language, to='en')

sentences = input_text.sentences

for sentence in sentences:
    print(sentence.sentiment)

#consider sentences
#Use the correct() method to attempt spelling correction.
#testimonial = TextBlob(inputText)
#language = testimonial.detect_language()
#print(language)
#testimonial.translate(from_lang=language, to='en')
#print(testimonial)
#print(testimonial.sentiment)


# nltk.download('punkt') -> for punctuation
# nltk needed to download punkt