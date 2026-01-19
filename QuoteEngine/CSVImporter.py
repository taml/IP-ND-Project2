from typing import List
import pandas

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

""" CSV Importer class, inherits from IngestorInterface """


class CSVImporter(IngestorInterface):
    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """ Class method to import and parse a CSV file
        :param path: string - Path to CSV file
        :return quotes: QuoteModel[] - An array of QuoteModel objects
        """
        if not cls.can_ingest(path):
            raise Exception(
                f'Cannot ingest {path}, please ensure that the path is '
                f'correct and the file type is CSV.'
            )

        quotes = []
        df = pandas.read_csv(path, header=0)

        for index, row in df.iterrows():
            new_quote = QuoteModel(row['body'].strip(' "'),
                                   row['author'].strip())
            quotes.append(new_quote)

        return quotes
