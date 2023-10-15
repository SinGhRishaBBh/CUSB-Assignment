#Python program to print Fibonacci series using iteration
def fibonacci_iteration(n):
    if n <= 0:
        return "Invalid input"  

    fib_series = [0, 1]  # Initialize the series with the first two Fibonacci numbers

    while len(fib_series) < n:
        next_number = fib_series[-1] + fib_series[-2]  # Calculate the next Fibonacci number
        fib_series.append(next_number)

    return fib_series


n = 10  
result = fibonacci_iteration(n)
print("Fibonacci series using iteration:")
print(result)
