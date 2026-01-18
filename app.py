import random
import os
import requests
from flask import Flask, render_template, abort, request

from QuoteEngine import TextIngestor
from MemeGenerator import MemeEngine

""" Create new Flask app"""
app = Flask(__name__)

""" Initialise the MemeEngine"""
meme = MemeEngine('./static')


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []
    for file in quote_files:
        quotes += TextIngestor.parse(file)

    images_path = "./_data/photos/dog/"

    imgs = []
    for (root, dirs, files) in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme
    :return: render_template: - template including HTML and path to random meme
    """
    img = None
    if len(imgs) > 0:
        img = random.choice(imgs)

    quote = None
    if len(quotes) > 0:
        quote = random.choice(quotes)

    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information
    :return: render_template: - template including meme generation form HTML
    """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme
    :return: render_template: - template including HTML and path to meme
    """
    image_url = request.form['image_url']
    body = request.form['body']
    author = request.form['author']

    if not all([image_url, body, author]):
        abort(400, description="Image URL, quote body, and "
                               "quote author are required.")

    try:
        req = requests.get(image_url, stream=True)
    except requests.exceptions.RequestException:
        abort(400, description="Failed to fetch image")

    tmp = f'./tmp_{random.randint(0, 10000000000)}.jpg'

    try:
        with open(tmp, 'wb') as img:
            img.write(req.content)

            path = meme.make_meme(tmp, body, author)

            if not path:
                abort(500, description="Failed to generate meme.")

    finally:
        if os.path.exists(tmp):
            os.remove(tmp)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
