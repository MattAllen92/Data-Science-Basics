s="aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"

# my long winded way
import string

def printer_error(s):
    errors = 0
    bad = string.lowercase[13:]
    for char in bad:
        errors += s.count(char)
    return "%d/%d" % (errors, len(s))

print printer_error(s)

# efficient way
def printer_error2(s):
    return "{}/{}".format(len([x for x in s if x not in "abcdefghijklm"]), len(s))

print printer_error2(s)

# NOTE: you can compare the 'value' of characters
for i in s:
    if i > "m":
        print i