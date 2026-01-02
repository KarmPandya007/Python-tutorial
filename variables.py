print("I like pizza")
print("Its really good")


# Variable : A container for value(string, integer, float, boolean)
            #  A variable behaves as if it was the value it contains

first_name = "Karm"
last_name = "Pandya"
age = 20
rupees = 10.99
isStudent = True
isOnline = False

age += age
age += 1

print("Hello " + first_name + " " + last_name)
print(f"Hello {first_name} {last_name}")
print(f"Your age is : {age}")
print(f"You have to pay : {rupees}")
print(type(first_name))
print(type(rupees))
print(type(isStudent))

if isStudent :
    print("You are a student")
else : {
    print("You aren't a student")
}
    
if isOnline :
    print("You are online")
else : {
    print("You aren't online")
}