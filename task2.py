class Calculator:
    def __init__(self, x, y, ch):
        self.num1 = x
        self.num2 = y 
        self.choice = ch

    def operation(self):
        if self.choice == 1:
            print(f"{self.num1} + {self.num2} = {self.num1 + self.num2}")
        elif self.choice == 2:
            print(f"{self.num1} - {self.num2} = {self.num1 - self.num2}")
        elif self.choice == 3:
            print(f"{self.num1} x {self.num2} = {self.num1 * self.num2}")
        elif self.choice == 4:
            if self.num2 != 0:
                print(f"{self.num1} / {self.num2} = {self.num1 / self.num2}")
            else:
                print("Error! Divide by Zero.")
        elif self.choice == 5:
            if self.num2 != 0:
                print(f"{self.num1} % {self.num2} = {self.num1 % self.num2}")
            else:
                print("Error! Divide by Zero.")
        else:
            print("Invalid Option.")
    
num1 = eval(input("Enter first number:"))
num2 = eval(input("Enter second number:"))
print("Menu")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulus")
choice = int(input("Enter your choice:"))
calc = Calculator(num1, num2, choice)
calc.operation()
