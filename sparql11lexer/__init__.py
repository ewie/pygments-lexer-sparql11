# -*- coding: utf-8 -*-
"""
Quick and dirty SPARQL 1.1 Lexer for Pygments

It's based on the Turtle Lexer from ``https://github.com/kierdavis/TurtleLexer``.

It is probably incomplete and even incorrect; feel free to contribute.
"""

from pygments.lexer import RegexLexer, bygroups
from pygments.formatter import Formatter
from pygments.token import *

PREFIX = r"[a-zA-Z][-_a-zA-Z0-9]*"
NAME = r"[_a-zA-Z][-_a-zA-Z0-9]*"

class Sparql11Lexer(RegexLexer):
  name = "SPARQL 1.1"
  aliases = ["sparql11"]
  filenames = ["*.sparql"]
  mimetypes = ["text/x-sparql", "text/sparql", "application/sparql"]
  
  tokens = {
    "root": [
      (r"#.*\n", Comment.Single),
      (r",|;|\.|\(|\)|\[|\]|\{|\}|\^\^", Punctuation),
      ("(%s)?\:(%s)?" % (PREFIX, NAME), Name.Tag),
      (r"_\:%s" % NAME, Name.Variable),
      (r"[\$\?]%s" % NAME, Name.Variable),
      (r"<[^>]*>", Name.Constant),
      (r"(['\"]).+\1", String.Double),
      (r"\d+(\.\d*)?([eE][+\-]?\d+)?", Number),
      (r"\.\d+([eE][+\-]?\d+)?", Number),
      (r"\s+", Whitespace),
      (r"true|false", Keyword.Constant),
      (r"(?i)prefix|select|construct|ask|describe|where|from|as|graph|filter"
        "|optional|a|union|not exists", Keyword.Reserved),
      (r"(?i)distinct|reduced|group by|order by|limit|offset|asc|desc",
       Keyword.Reserved),
      (r"(?i)count|sum|avg|min|max|groupconcat|sample",
       Keyword.Reserved),
      (r"(?i)delete|insert|data|load|clear|create|drop|copy|move|add",
       Keyword.Reserved),
      (r"(?i)regex",
       Keyword.Function),
      (r"\+|-|\*|/|=|!|<|>|\&|\|", Punctuation),
      (r".+", Error),
    ],
  }

def setup(app):
    """Register Sparql11Lexer to Sphinx"""
    sparqlLexer = Sparql11Lexer()
    app.add_lexer('sparql11', sparqlLexer)
