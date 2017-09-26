###########################################################
# Strings
### format replaces {} with a specifed string value
##word1 = input("Enter a word:") # good for handling user input
##word2 = input("Enter a word:")
##word3 = input("Enter a word:")
##
##test = "{} and {} but not {}".format(word1, word2, word3)
##print test

# String manipulation
##split
##replace
##slicing
##indexof
##reverse
##escaping
##format
##join
##in/not in
##concatenate
##upper/lower

##test = "Hello. My name is James. Alright?"
##test2 = test.split('.')
##print test2
##
##test = "My mother married my monarch."
##test2 = test.replace('m','@')
##print test2
##
##test = "Hello, World!"
##print test[:5]
##print test[3:]
##print test.index('l')
##print test[-1]
##for i in test[::-1]:
##    print i
##test = "Then she said \"OK\"."
##test = "But not before saying 'No'"
##test = 'This is also "fine"'
##test = "Hi, {} is my {}.".format("Matt","name")
##test_list = ["Hi","my","name","is","Matt"]
##print " ".join(test_list)
##print "Hi" in test
##print "Hello" not in test
##test = "Hello"
##test2 = ", World!"
##print test + test2
##print test * 3
##test = "HeLlO"
##print test.upper()
##print test.lower()
##print test.capitalize()

### enumerate - indexes items in an iterable
##tv = [1,2,3]
##test = enumerate(tv)
##for i, j in test:
##    print i, j

### break
##for i in xrange(0,100):
##    print i
##    break

##while True:
##    print("Press q to quit")
##    a = input("Enter a letter:")
##    if a == "q":
##        break
##    else:
##        continue

###########################################################

### Modules
### Built-in and pre-designed
##import math
###import statistics
##import random
##import keyword
##
##print random.randint(0,100)
##print math.pow(2,3)
###print statistics.mean([1,4,6,2,3,4,6])
##print keyword.iskeyword("for")

# My own module

