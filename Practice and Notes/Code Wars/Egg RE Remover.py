import re

def unscrambled_eggs(word):
    return re.sub(r"egg", "", word)

print unscrambled_eggs("testeggtestegg")