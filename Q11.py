#Python program to check whether the given integer is a prime number or not

num = int(input("Enter any number: "))

# prime number is always greater than 1
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")

# if the entered number is less than or equal to 1
else:
    print(num, "is not a prime number")

