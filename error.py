while True:
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        result = num1/num2
        print(result)
        break
    except ValueError:
        print("Invalid input.Please enter numeric values")