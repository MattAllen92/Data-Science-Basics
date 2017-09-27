colours = {0:"black",1:"brown",2:"red",3:"orange",4:"yellow",5:"green",6:"blue",7:"violet",8:"gray",9:"white"}

def encode_resistor_colors(ohms_string):
    ohms = 0
    power = 0
    first = ohms_string.split(" ")[0]
    if "k" in first:
        ohms = int(float(first.replace("k","")) * 1000)
    elif "M" in first:
        ohms = int(float(first.replace("M","")) * 1000000)
    else:
        ohms = int(first)
    first_char = int(str(ohms)[0])
    second_char = int(str(ohms)[1])
    if str(ohms)[2:]:
        power = len(str(ohms)[2:])
    return colours[first_char] + " " + colours[second_char] + " " + colours[power] + " gold"
    
print encode_resistor_colors("1k ohms")