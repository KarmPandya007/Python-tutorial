# Exercise 2 : Shopping Cart Problem

item = input("What would you like to buy : ")
price = float(input("What is the price : "))

quantity = int(input("How many would you like : "))

total = price * quantity

if quantity==0 or quantity<0  : 
    print(f"Quantity cant be this low!")
elif quantity==1 : 
    print(f"The price of {quantity} {item} will be {total}")
elif quantity>1 : 
    print(f"The price of {quantity} {item}s will be {total}")
else :
    print("Quantity issue!")
