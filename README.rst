SPARQL Lexer for Pygments
=========================

This is a lexer for syntax-highlighting SPARQL_ queries with Pygments_.

It can be used as a Sphinx_ extension.

.. _SPARQL: http://www.w3.org/TR/sparql11-overview/
.. _Pygments: http://pygments.org/
.. _Sphinx: http://sphinx-doc.org/

Using the Lexer in Sphinx
-------------------------

Add the following line to your ``conf.py`` file:

.. code-block:: python

    EXTDIR = '../ext' # ... or wherever you decided to put your extensions
    sys.path.insert(0, os.path.abspath(EXTDIR))
    extensions += ['sparqllexer']
