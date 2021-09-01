a = float(input('Enter number: '))
b = float(input('Enter another number: '))
c = input('Enter sign: ')

def add(num1, num2):
    return num1 + num2

def minus(num1, num2):
    return num1 - num2

def multi(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

def init():

    if c != "+" and c != "-" and c != "*" and c != "/":
        print("Operator does not exist")
    
    else:
        if c == "+":
            print(add(a, b))
        
        elif c == "-":
            print(minus(a, b))
    
        elif c == "*":
            print(multi(a, b))
        
        elif c == "/":
            print(div(a, b))
        
        else: 
            pass

init()
