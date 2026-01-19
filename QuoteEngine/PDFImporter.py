from typing import List
import subprocess
import os
import random

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


""" PDF Importer class, inherits from IngestorInterface """


class PDFImporter(IngestorInterface):
    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """ Class method to import and parse a PDF file
        :param path: string - Path to PDF file
        :return quotes: QuoteModel[] - An array of QuoteModel objects
        """
        if not cls.can_ingest(path):
            raise Exception(
                f'Cannot ingest {path}, please ensure that the path is '
                f'correct and the file type is PDF.'
            )

        tmp = f'./tmp/{random.randint(0, 100000000)}.txt'
        call = subprocess.call(['pdftotext', path, tmp])

        file_ref = open(tmp, "r")
        quotes = []

        for line in file_ref.readlines():
            line = line.strip('\n\r').strip()
            if len(line) > 0:
                parse = line.split('-')
                new_quote = QuoteModel(parse[0].strip(' "'), parse[1].strip())
                quotes.append(new_quote)
        file_ref.close()
        os.remove(tmp)
        return quotes
