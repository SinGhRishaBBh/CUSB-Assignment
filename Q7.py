#Python program to find the geometric mean of n numbers

def geometric_mean(numbers):

   product = 1

   for number in numbers:

       product *= number

   return product ** (1 / len(numbers))


numbers = [int(x) for x in input("Enter n numbers separated by spaces: ").split()]

mean = geometric_mean(numbers)

print("Geometric Mean:", mean)

