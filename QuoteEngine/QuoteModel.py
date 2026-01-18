""" QuoteModel class """


class QuoteModel:
    """ QuoteModel constructor
    :param body: The body of the quote
    :param author: The author of the quote
    """
    def __init__(self, body, author):
        self.body = body
        self.author = author

    def quote(self):
        """ Return the quote """
        return f'”{self.body}” - {self.author}'

    def __repr__(self):
        """ Return a string representation of the quote """
        return f'<{self.body}, {self.author}>'
