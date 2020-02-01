#Program to take in a range of numbers and print out a random number within that range
import random
print("Hello, This program allows you to specify a number range and get a random number within that range")
bottomrange = int(input('Please specify lowest number in required range: '))
toprange = int(input('Please highest number in required range: '))

randnum = random.randint(bottomrange,toprange)
print("here is a random number within your specified range {}".format(randnum))