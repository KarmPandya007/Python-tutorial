# Weight Converter : 

weight = float(input("Enter your weight : "))
unit = input("Enter the unit of the weight that you entered above (K - kilograms, L - pounds) : ")

if unit == "K" or unit == "k" : 
    weight = weight * 2.205
    unit = "lbs"
elif unit == "L" or unit == "l" : 
    weight = weight / 2.205
    unit = "kgs"
else : 
    print(f"{unit} is not a valid unit!")

print(f"Your weight in {unit} is {weight} {unit}!")
