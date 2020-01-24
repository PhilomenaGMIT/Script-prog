# This program calculates a person's body mass index from their height and weight.
#The preson must enter their height in cms and weight in kg and the porgram calculates and outputs their BMI 

height = float(input("Please enter your height in cms: "))
weight = float(input("Please enter your weight in kgs: "))

# convert height to metres 
heightM = height/100

bmi = float (weight / (heightM ** 2))

print("Thank You. Your BMI has been calculated as ",bmi)