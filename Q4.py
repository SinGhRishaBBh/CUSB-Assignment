#Python program to find the circumference and area of a circle with a given radius.

r = float(input("Enter the radius of the circle "))
pi = 3.14
circumference = 2*pi*r
area = pi*(r**2)
print("The circumference of the circle is ", circumference)
print("The area of the circle is ", area)