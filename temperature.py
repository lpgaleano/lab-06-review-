tempincelsius = input("please enter a Temperature in celsius... ")
tempinfahernheit = float(tempincelsius * 1.8 + 32).toFixed(2)
tempincelsius = round(tempinfahernheit, 2)
#.toFixed is a method used to limit the number of decimal placers
print(str(tempincelsius) + " degrees celseius is " + str(tempinfahernheit) + " degree Farenheit.")
