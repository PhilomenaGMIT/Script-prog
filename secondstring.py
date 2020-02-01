# This program takes in a string and outputs every second letter in reveres order.


instring = input("Please enter a random string: ")

length = len(instring)

# get every second character
print (instring[length:0:-2])


