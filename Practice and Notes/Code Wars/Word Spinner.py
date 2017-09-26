# my long winded method
def spin_words(sentence):
    output = []
    for word in sentence.split():
        if len(word) < 5:
            output.append(word)
        else:
          output.append(word[::-1])
    return ' '.join(output)

print spin_words("Hey fellow warriors")

# elegant method
def spin_words2(sentence):
    return " ".join([x[::-1] if len(x) > 5 else x for x in sentence.split()])

print spin_words2("Hey fellow warriors")