class Calculator:
    def add(self, a, b=None):
        if b is not None:
            print(a + b)
        else:
            print(a + a)  

# Create an instance
calc = Calculator()

# Using the method with two arguments
calc.add(5, 3)

# Using the method with one argument
calc.add(7)