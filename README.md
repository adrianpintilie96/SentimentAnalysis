# Sentiment Analysis

## The purpose of this small project is to build a sentence to emoji app.

### The project has two main components:
  1. A RESTful API service that receives a sentence and according to its emotion will return the appropriate emoji.
  2. A simple web application that uses this API
  
#### The application was build using the micro web framework Flask. 
#### The sentence to emoji service uses TextBlob, a library for processing textual data. By computing the polarity of the sentence using a Naive Bayes Classifier trained on a movie reviews corpus, we can map the sentence to the appropriate emoji.
