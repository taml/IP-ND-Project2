from abc import ABC, abstractmethod
from typing import List

from .QuoteModel import QuoteModel


""" Ingestor interface, inherits from ABC class """


class IngestorInterface(ABC):

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path) -> bool:
        """ Check if an ingestor is allowed to ingest a file
        :param path: string - path to file
        :return ext: bool - whether the file can be ingested
        """
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse a file into a list of QuoteModels
        :param path: string - path to file
        :return: List[QuoteModel]
        """
        pass
