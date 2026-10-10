firstNum, secondNum, operation = float(input()), float(input()), input()
if operation == '+':
    print(firstNum + secondNum)
if operation == '-':
    print(firstNum - secondNum)
if operation == '*':
    print(firstNum * secondNum)
if operation == '/':
    if secondNum == 0:
        print("Ошибка")
    else:
        print(firstNum / secondNum)