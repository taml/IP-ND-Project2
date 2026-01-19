from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


""" TXT Importer class, inherits from IngestorInterface """


class TXTImporter(IngestorInterface):
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """ Class method to import and parse a TXT file
        :param path: string - Path to TXT file
        :return quotes: QuoteModel[] - An array of QuoteModel objects
        """
        if not cls.can_ingest(path):
            raise Exception(
                f'Cannot ingest {path}, please ensure that the path is '
                f'correct and the file type is TXT.'
            )

        quotes = []

        with open(path, 'r') as file:
            for line in file.readlines():
                line = line.strip('\n\r').strip()
                if len(line) > 0:
                    parse = line.split('-')
                    new_quote = QuoteModel(parse[0].strip(' "'),
                                           parse[1].strip())
                    quotes.append(new_quote)

        return quotes
