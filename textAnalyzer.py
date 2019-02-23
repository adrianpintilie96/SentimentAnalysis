
import nltk
from textblob import TextBlob

#nltk.download()
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA

sia = SIA()

#line = 'I’m very happy that my team won the world cup!'
line = 'Eu sunt fericit'

pol_score = sia.polarity_scores(line)

print(pol_score)


#consider sentences
#Use the correct() method to attempt spelling correction.
testimonial = TextBlob(line)
language = testimonial.detect_language()
print(language)
testimonial.translate(from_lang=language, to='en')
print(testimonial)
print(testimonial.sentiment)