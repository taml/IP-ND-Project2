import os
import random
import argparse

from QuoteEngine import TextIngestor, QuoteModel
from MemeGenerator import MemeEngine


def generate_meme(path=None, body=None, author=None):
    """ Generate a meme given a path and a quote
    :param path: string - path to image used for meme
    :param body: string - body of the meme
    :param author: string - author of the body quote
    :return: path: string - path to the new meme
    """
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(TextIngestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    meme = MemeEngine('./tmp')
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
    """ Parse command line arguments
    --path: string - (optional) path to image used for meme
    --body: string - (optional) body of the meme
    --author: string - (optional if no body is provided) author of
                       the body quote

    Random image and content will be used if arguments are omitted
    """
    parse = argparse.ArgumentParser(
        description='Generate a meme given a path, a quote body and an author')
    parse.add_argument('--path', type=str, default=None,
                       help='The path of the meme image')
    parse.add_argument('--body', type=str, default=None,
                       help='The body of the meme image')
    parse.add_argument('--author', type=str, default=None,
                       help='The author of the meme image')
    args = parse.parse_args()

    print(generate_meme(args.path, args.body, args.author))
