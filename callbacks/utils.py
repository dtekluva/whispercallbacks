from rest_framework.parsers import BaseParser


# Create your utility function(s) and class(es) here.
class PlainTextParser(BaseParser):
    """Plain text parser."""

    media_type = "text/plain"

    def parse(self, stream, media_type=None, parser_context=None):
        """
        Simply return a string representing the body of the request.
        """
        return stream.read()
