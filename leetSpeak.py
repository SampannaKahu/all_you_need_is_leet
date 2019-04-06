# -*- coding: utf-8 -*-
from unicodedata import *

leetMap = {'a': 'CYRILLIC SMALL LETTER A',
           'A': 'CYRILLIC CAPITAL LETTER A',
           'b': 'CYRILLIC CAPITAL LETTER SOFT SIGN',
           'B': 'CYRILLIC CAPITAL LETTER VE',
           'c': 'CYRILLIC SMALL LETTER ES',
           'C': 'CYRILLIC CAPITAL LETTER ES',
           'd': 'CYRILLIC SMALL LETTER KOMI DE',
           'D': 'CHEROKEE LETTER A',
           'e': 'CYRILLIC SMALL LETTER IE',
           'E': 'CYRILLIC CAPITAL LETTER IE',
           'f': 'LATIN SMALL LETTER LONG S WITH HIGH STROKE',
           'F': 'LISU LETTER TSA',
           'g': 'ARMENIAN SMALL LETTER CO',
           'G': 'CYRILLIC CAPITAL LETTER KOMI SJE',
           'h': 'CYRILLIC SMALL LETTER SHHA',
           'H': 'CYRILLIC CAPITAL LETTER EN',
           'i': 'CYRILLIC SMALL LETTER BYELORUSSIAN-UKRAINIAN I',
           'I': '|',
           'j': 'CYRILLIC SMALL LETTER JE',
           'J': 'CYRILLIC CAPITAL LETTER JE',
           'k': 'CYRILLIC CAPITAL LETTER KA',
           'K': 'CYRILLIC CAPITAL LETTER KA',
           'l': 'COPTIC CAPITAL LETTER IAUDA',
           'L': 'CHEROKEE LETTER TLE',
           'm': 'CYRILLIC CAPITAL LETTER EM',
           'M': 'CYRILLIC CAPITAL LETTER EM',
           'n': 'ARMENIAN SMALL LETTER VO',
           'N': 'GREEK CAPITAL LETTER NU',
           'o': 'CYRILLIC SMALL LETTER O',
           'O': 'CYRILLIC CAPITAL LETTER O',
           'p': 'CYRILLIC SMALL LETTER ER',
           'P': 'CYRILLIC CAPITAL LETTER ER',
           'q': 'CYRILLIC SMALL LETTER QA',
           'Q': 'TIFINAGH LETTER YARR',
           'r': 'CYRILLIC SMALL LETTER GHE',
           'R': 'LISU LETTER ZHA',
           's': 'CYRILLIC SMALL LETTER DZE',
           'S': 'CYRILLIC CAPITAL LETTER DZE',
           't': 'CYRILLIC CAPITAL LETTER TE',
           'T': 'CYRILLIC CAPITAL LETTER TE',
           'u': 'LATIN LETTER SMALL CAPITAL U',
           'U': 'ARMENIAN CAPITAL LETTER SEH',
           'v': 'CYRILLIC SMALL LETTER IZHITSA',
           'V': 'TIFINAGH LETTER YADH',
           'w': 'CYRILLIC SMALL LETTER WE',
           'W': 'CYRILLIC CAPITAL LETTER WE',
           'x': 'CYRILLIC SMALL LETTER HA',
           'X': 'CYRILLIC CAPITAL LETTER HA',
           'y': 'CYRILLIC SMALL LETTER U',
           'Y': 'CYRILLIC CAPITAL LETTER STRAIGHT U',
           'z': 'LATIN LETTER SMALL CAPITAL Z',
           'Z': 'CHEROKEE LETTER NO'
           }


def word2Leet(word, num):
    if (num < 0):
        return word

    leetWord = ''
    changeLen = min(len(word), num)
    for i in range(changeLen):
        if word[i] not in leetMap:
            continue
        leetCode = leetMap[word[i]]
        leetChar = lookup(leetCode)
        leetWord += leetChar
    for i in range(changeLen, len(word)):
        leetWord += word[i]
    return leetWord
