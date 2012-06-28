#!/usr/bin/env python
# -*- coding: utf-8 -*-

import functools
import sys

def iterunique(sequence):
    """Yield elements not encountered before"""
    known_elements = set()
    for element in sequence:
        if element in known_elements:
            pass
        else:
            known_elements.add(element)
            yield element

def unique_stdin_stdout():
    """Print to stdout lines in stdin not encountered before"""
    try:
        iterable = iter(functools.partial(raw_input), None)
        for unique_element in iterunique(iterable):
            print unique_element
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
