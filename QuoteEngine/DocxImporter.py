from typing import List
import docx

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


""" Docx Importer class, inherits from IngestorInterface """


class DocxImporter(IngestorInterface):
    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """ Class method to import and parse a Docx file
        :param path: string - Path to Docx file
        :return quotes: QuoteModel[] - An array of QuoteModel objects
        """
        if not cls.can_ingest(path):
            raise Exception(
                f'Cannot ingest {path}, please ensure that the path is '
                f'correct and the file type is Docx.'
            )

        quotes = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                parse = para.text.split('-')
                new_quote = QuoteModel(parse[0].strip(' "'), parse[1].strip())
                quotes.append(new_quote)

        return quotes
