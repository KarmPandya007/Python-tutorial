# Calculator : 

num1 = float(input("Enter the first number : "))
num2 = float(input("Enter the second number : "))

operator = input("Enter the operator (+, -, *, /, %) : ")
if operator=="+" :
    print(f"The addition of the numbers is : {num1+num2}")
elif operator=="-" :
    print(f"The difference between the numbers is : {num1-num2}")
elif operator=="*" :
    print(f"The product of the numbers is : {num1*num2}")
elif operator=="/" :
    print(f"The division of the numbers is : {num1/num2}")
elif operator=="%" :
    print(f"The remainder of the numbers is : {num1%num2}")
else :
    print(f"{operator} is not a valid operator")
 