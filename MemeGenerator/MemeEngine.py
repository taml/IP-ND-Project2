import os
from PIL import Image, ImageDraw, ImageFont
import PIL
import random
import textwrap


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
            ratio = width / float(img.size[0])
            height = int(ratio * float(img.size[1]))

            img = img.resize((width, height), Image.NEAREST)

            if text is not None and author is not None:
                draw = ImageDraw.Draw(img)
                text_lines = textwrap.wrap(text, width=40)
                font = ImageFont.truetype('./fonts/Chewy-Regular.ttf', size=20)

                bounding_box = draw.multiline_textbbox(
                    (0, 0),
                    "{} - {}".format('\n'.join(text_lines), author),
                    font=font
                )
                text_width = bounding_box[2] - bounding_box[0]
                text_height = bounding_box[3] - bounding_box[1]

                if width - text_width - 20 < 10:
                    position_x = 10
                else:
                    position_x = random.randint(
                        10,
                        width - int(text_width) - 10
                    )

                if height - text_height - 20 < 10:
                    position_y = 10
                else:
                    position_y = random.randint(
                        10,
                        height - int(text_height) - 10
                    )

                draw.multiline_text(
                    (position_x, position_y),
                    "{} - {}".format('\n'.join(text_lines), author),
                    font=font,
                    fill='white'
                )

            out_path = os.path.join(
                self.output_dir,
                f"{random.randint(0, 100000)}-meme.png"
            )
            img.save(out_path)
            return out_path
        except PIL.UnidentifiedImageError as e:
            raise ValueError(f"Invalid image file: {img_path}") from e
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Image file not found: {img_path}") from e
