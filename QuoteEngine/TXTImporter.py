from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TXTImporter(IngestorInterface):
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest exception')

        quotes = []

        with open(path, 'r') as file:
            for line in file.readlines():
                line = line.strip('\n\r').strip()
                if len(line) > 0:
                    parse = line.split('-')
                    new_quote = QuoteModel(parse[0].strip(' "'), parse[1].strip())
                    quotes.append(new_quote)

        return quotes

