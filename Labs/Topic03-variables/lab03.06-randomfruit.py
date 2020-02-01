#Program to print out a random fruit

import random

Fruitlist = ['Apple','Orange','Pear','Melon','Lemon','Pineapple','Banana']
listlength = len(Fruitlist)
randomindex = random.randint(0,listlength-1)


print("Here is a random fruit: {}".format(Fruitlist[randomindex]))