#!/usr/bin/env python

from re import sub

class Converter():

    """
    String manipulation.
    """

    def to_underscore(self, string):
        str = sub('(.)([A-Z][a-z]+)', r'\1_\2', string)
        return sub('([a-z0-9])([A-Z])', r'\1_\2', str).lower()

    def to_camelcase(self, string):
        str = sub(r'_([a-zA-Z])', lambda m: m.group(1).upper(), string)
        return str[0].upper() + str[1:]