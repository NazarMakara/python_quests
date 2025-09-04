num1 = input("Enter first num: ")
sign = input("Enter a sign: ")
num2 = input("Enter second num: ")
sings = ("+", "-", "*", "/")
if sign not in sings:
    print("error")
else:
    num1 = float(num1)
    num2 = float(num2)
    if sign == "+":
        print(num1 + num2)
    elif sign == "-":
        print(num1 - num2)
    elif sign == "*":
        print(num1 * num2)
    elif sign == "/":
        print(num1 / num2)