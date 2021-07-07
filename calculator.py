def control(num1, operator, num2):
    if operator == "+":
        result = num1 + num2
        print('>> ' + str(result))
    elif operator == "*":
        result = num1 * num2
        print('>> ' + str(result))
    elif operator == "-":
        result = num1 - num2
        print('>> ' + str(result))
    elif operator == "/":
        result = num1 / num2
        print('>> ' + str(result))
    else:
        print("Invalid operator")

number1 = int(input('First number: '))
op = input("math operator: ")
number2 = int(input("Second number: "))

control(number1, op, number2)


def some():
    print("hello some ")
