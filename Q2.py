#Python program to find the area of a triangle whose sides are given

a = float(input("Enter side of first side of triangle"))
b = float(input("Enter side of seconf side of triangle"))
c = float(input("Enter side of third side of triangle"))

s=(a+b+c)/2 
#Area calculation
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5

#Print the output
print('The area of the triangle is %0.2f' %area)

