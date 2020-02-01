#Program to take in a string, remove leading or trailing blanks, convert to lower case and output details

inputstring = input('Please enter any string of characters: ')
inlength = len(inputstring)
outputstring = inputstring.strip().lower()

inlength = len(inputstring)
outlength = len(outputstring)

print("That string normalised is {}".format(outputstring))
print("We reduced the length from {} to {} characters".format(inlength,outlength))