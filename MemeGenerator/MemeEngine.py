import os

from .Meme import Meme
from PIL import Image, ImageDraw, ImageFont
import random

# Loading of a file from disk
# Transform image by resizing to a maximum width of 500px while maintaining the input aspect ratio
# Add a caption to an image (string input) with a body and author to a random location on the image.

class MemeEngine:
    def __init__(self, output_dir):
        self.output_dir = output_dir
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    def make_meme(self, img_path, text, author, width=500) -> str:
        try:
            img = Image.open(img_path)

            if width is not None:
                ratio = width / float(img.size[0])
                height = int(ratio * float(img.size[1]))
                img = img.resize((width, height), Image.NEAREST)

            if text is not None and author is not None:
                draw = ImageDraw.Draw(img)
                #font = ImageFont.truetype('./fonts/LilitaOne-Regular.ttf', size=20)
                #draw.text((10, 30), message, font=font, fill='white')
                draw.text((10, 30), f"{text} - {author}", fill='white')

            out_path = os.path.join(self.output_dir, f"{random.randint(0, 100000)}-meme.png")
            img.save(out_path)
            return out_path
        except FileNotFoundError:
            return ''