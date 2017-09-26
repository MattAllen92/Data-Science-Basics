def alphabet_position(text):
    alpha = list("abcdefghijklmnopqrstuvwxyz")
    out = []
    for char in text:
        if char.isalpha():
            out.append(str(alpha.index(char.lower())+ 1))
    return ' '.join(out)

print alphabet_position("The narwhal bacons at midnight.")