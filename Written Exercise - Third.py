expression = "5 1 .2 + 4.1 * + 3 - SQRT"
stack = []
environment = {}

binary_operations = {
    '+': lambda x,y: x + y,
    '-': lambda x,y: x - y,
    '*': lambda x,y: x * y,
    '/': lambda x,y: x / y,
    '**': lambda x,y: x ** y,
}

unary_operations = {
    'SQRT': lambda x: x**0.5,
    'SQR' : lambda x: x**2,
}

def tokenize(input_string):
    split_values = []
    b = ''
    for a in input_string:
        if a == ' ' and b != '':
            split_values.append(b)
            b = ''
        else:
            b += a
    if b != '':
        split_values.append(b)
    return split_values

def number_check(x):
    try:
        float(x)
        return True
    except ValueError:
        return False

def evaluate(expression, stack, binary_operations, unary_operations):
    while(True):
        expression = input("WHAT WOULD YOU LIKE TO COMPUTE? ")
        if expression == "QUIT":
            break
        elif expression == "PRINT":
            print(stack)
            break
        else:
            boo = False
            for c in tokenize(expression):
                if number_check(c) == True:
                    stack.append(float(c))
                    boo = True
                elif c in unary_operations:
                    if len(stack) == 0:
                        print("There are not enough numbers in the stack for this calculation. Sorry!")
                        del stack[:]
                        boo = False
                        break
                    else:
                        stack.append(unary_operations[c](stack.pop()))
                        boo = True
                elif c in binary_operations:
                    if len(stack) < 2:
                        print("There are not enough numbers in the stack for this calculation. Sorry!")
                        del stack[:]
                        boo = False
                        break
                    else:
                        stack.append(binary_operations[c](stack.pop(-2),stack.pop(-1)))
                        boo = True
                elif c == "STORE":
                    e = stack.pop()
                    environment[e] = stack.pop()
                    boo = False
                elif c == "LOAD":
                    if stack[-1] not in environment:
                        print("This variable is not in the environment. Sorry!")
                        del stack[:]
                        boo = False
                    else:
                        d = environment[stack.pop()]
                        stack.append(d)
                        boo = False
                else:
                    stack.append(c)
                    boo = False
            if boo == True:
                print("I CALCULATED:", stack[-1])

evaluate(expression, stack, binary_operations, unary_operations)
