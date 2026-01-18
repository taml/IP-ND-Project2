import os
from PIL import Image, ImageDraw, ImageFont
import PIL
import random


""" Meme Engine class """


class MemeEngine:
    """ Meme Engine constructor
    :param output_dir: string - the directory to save the generated meme
    """
    def __init__(self, output_dir):
        self.output_dir = output_dir
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    def make_meme(self, img_path, text, author, width=500) -> str:
        """ Make a meme given a path and a quote
        :param img_path: string - the path of the image to be used in the meme
        :param text: string - text of the meme quote
        :param author: string - author of the meme quote
        :param width: int - number between 0 and 500 for meme width
        :return: string - path to new meme image
        """
        if width > 500 or width <= 0:
            raise Exception('Width must be greater than 0 '
                            'and less than or equal to 500')

        try:
            img = Image.open(img_path)

            if width is not None:
                ratio = width / float(img.size[0])
                height = int(ratio * float(img.size[1]))
                img = img.resize((width, height), Image.NEAREST)

            if text is not None and author is not None:
                draw = ImageDraw.Draw(img)
                # font = ImageFont.truetype('./fonts/LilitaOne-Regular.ttf', size=20)
                # draw.text((10, 30), message, font=font, fill='white')
                draw.text((10, 30), f"{text} - {author}", fill='white')

            out_path = os.path.join(self.output_dir,
                                    f"{random.randint(0, 100000)}-meme.png")
            img.save(out_path)
            return out_path
        except PIL.UnidentifiedImageError:
            return ''
        except FileNotFoundError:
            return ''
