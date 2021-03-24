# each character in the new string is "(" if that character appears only once in the original string
# or ")" if that character appears more than once in the original string

def duplicate_encode(word):
    return "".join(["(" if word.lower().count(x) == 1 else ")" for x in word.lower()])



