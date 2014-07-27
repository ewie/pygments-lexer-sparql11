#!/usr/bin/python

from setuptools import setup, find_packages

setup(
    name='pygments-lexer-sparql11',
    version='0.1',
    description='Pygments lexer for SPARQL 1.1',
    long_description=open('README.rst').read(),
    keywords='pygments sparql lexer',

    author='Pierre-Antoine Champin, Erik Wienhold',

    url='https://github.com/ewie/pygments-sparql11-lexer',

    packages=find_packages(),
    install_requires=['pygments >= 1.6'],

    entry_points='''[pygments.lexers]
                    sparql11=sparql11lexer:Sparql11Lexer'''
)
