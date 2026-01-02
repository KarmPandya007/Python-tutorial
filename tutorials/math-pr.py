import math


x = 25
y = 9.2

print(math.pi)
print(math.e)

result1 = math.sqrt(25)
result2 = math.ceil(y)
result3 = math.floor(y)

print(result1)
print(result2)
print(result3)


# Area of circle : pie*r^2

radius= float(input("Enter the radius of the circle : "))

area = math.pi*pow(radius, 2)

# Circumference of a circle :

circumference = 2*math.pi*radius

print(f"The area of the circle is : {area}")
print(f"The circumference of the circle is : {circumference}")



# the other longest side of a right angled triangle : 
a = float(input("Enter side a : "))
b = float(input("Enter side b : "))
c = math.sqrt(pow(a, 2) + pow(b, 2))
print(f"The length of the hypotenuse is : {c}")
