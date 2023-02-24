num1 = float(input("Enter a number: "))
opr = input("Enter a operator:")
num2 = float(input("Enter another number: "))

if opr == "+":
    print(num1 + num2)
elif opr == "-":
    print(num1 - num2)
elif opr == "/":
    print(num1 / num2)
elif opr == "*":
    print(num1 * num2)
else:
    print("Please enter a valid operator.")
