#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import locale
import HTMLParser
import functools
import sys

sys.stdout = codecs.getwriter(locale.getpreferredencoding())(sys.stdout);

def unique_stdin_stdout():
    """Print to stdout lines in stdin not encountered before"""
    h = HTMLParser.HTMLParser()
    try:
        iterable = iter(functools.partial(raw_input), None)
        for element in iterable:
            print h.unescape(element)
    except IOError, EOFError:
        sys.exit(0)


def cli():
    try:
        import argparse
        parser = argparse.ArgumentParser(description="Print unique lines.")
        prova = parser.parse_args()
    except ImportError:
        pass

if __name__ == "__main__":
    cli()
    unique_stdin_stdout()
