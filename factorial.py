
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Call the function and print the result
number = 5
factorial_of_5 = factorial(number)
print("The factorial of", number, "is", factorial_of_5)
