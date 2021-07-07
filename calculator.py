def control(num1, op, num2):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2


try:
    number1 = int(input("Number1>"))
    operator = input("Operator>")
    number2 = int(input("Number2>"))
    print(control(number1, operator, number2))
except ValueError:
    print("Value Error !")

