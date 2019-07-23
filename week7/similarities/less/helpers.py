# Modules
from nltk.tokenize import sent_tokenize


def lines(a, b):
    """Return lines in both a and b"""

    linesA = set(a.split("\n"))
    linesB = set(b.split("\n"))

    return linesA & linesB


def sentences(a, b):
    """Return sentences in both a and b"""

    sentencesA = set(sent_tokenize(a))
    sentencesB = set(sent_tokenize(b))

    return sentencesA & sentencesB

def tokenize_substring(str, n):
    substrings = []

    for i in range(len(str) - n + 1):
        substrings.append(str[i:i + n])

    return substrings

def substrings(a, b, n):
    """Return substrings of length n in both a and b"""
   
    a_substrings = set(tokenize_substring(a, n))
    b_substrings = set(tokenize_substring(b, n))

    return a_substrings & b_substrings