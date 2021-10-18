import sys
print("BMI: Body Mass Index Calculator v.0.1 beta")
userWeight = input("enter your weight (in pounds):")
userHeight = input("enter your height (in inches):")

myBMI = (703 * float(userWeight)) / (float(userHeight) * float(userHeight))
myBMI = round(myBMI, 2)
print("your body mass index (BMI) is " + str(myBMI) +"%")
