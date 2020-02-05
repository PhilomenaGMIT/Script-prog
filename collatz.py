# Program to take in any positive integer and perform a loop of successive caclulations and output the successive values as follows:
# Each step of the loop calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one. 
# Program ends when current value is one.

Inputint = int(input ("Please enter a positive integer: "))
i = Inputint

i = 1

if Inputint > 0 :
    i = Inputint
    
    
    while i > 1:
        if i % 2 == 0 :
            i = i/2
        else:
            i = (i * 3) +1

        print ("Current value is now ",i)  

         
else :
    print ("that is not a positive integer")