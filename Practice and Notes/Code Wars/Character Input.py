name = raw_input("Please enter your first name: ")
age = raw_input("Please enter your age in years: ")
repeat = raw_input("How many answers would you like? ")

print "Hello %s!" % name
time = 2017 + (100-int(age))
print "You are %s, you will turn 100 in the year %d!" % (age, time)
print "This many answers!" * int(repeat)

#print ("Hello {}! You will turn 100 in the year {}.".format(name, str(2017 + (100 - age))))*repeat