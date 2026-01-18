from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from .CSVImporter import CSVImporter
from .DocxImporter import DocxImporter
from .PDFImporter import PDFImporter
from .TXTImporter import TXTImporter


""" TextIngestor class, inherits from IngestorInterface """


class TextIngestor(IngestorInterface):
    importers = [CSVImporter, DocxImporter, PDFImporter, TXTImporter]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """ Parse a text file into a list of QuoteModel objects.
        :param path: string - path to the text file to parse.
        :return: List[QuoteModel]
        """
        for importer in cls.importers:
            if importer.can_ingest(path):
                return importer.parse(path)
