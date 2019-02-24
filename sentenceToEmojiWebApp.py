from flask import Flask, render_template, request, url_for
from flask_bootstrap import Bootstrap
import requests

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/analyze', methods=['POST'])
def analyze():
    if request.method == 'POST':
        input_text = request.form['rawtext']
        url = 'http://127.0.0.1:5000/analyze/'+input_text
        response = requests.get(url).json()
        image_source = response['category']
		#todo: path of the image is not ok
        return render_template('home.html', received_text=input_text, image_source=image_source)


if __name__ == '__main__':
    app.run(debug=True, port=90)

# flask bootstrap
#cache the data?
