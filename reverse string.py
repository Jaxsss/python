# detects pangram

import string

alphabet = set(string.ascii_lowercase)

def is_pangram(s):
    return set(s.lower()) >= alphabet



