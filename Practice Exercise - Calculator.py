expression = "5 1 .2 + 4.1 * + 3 - SQRT"
split_values = []
stack = []

binary_operations = {
    '+': lambda x,y: x + y,
    '-': lambda x,y: x - y,
    '*': lambda x,y: x * y,
}

unary_operations = {
    'SQRT': lambda x: x**0.5,
}

def tokenize(input_string):
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
    for c in tokenize(expression):
        if number_check(c) == True:
            stack.append(float(c))
        elif c in unary_operations:
            stack.append(unary_operations[c](stack.pop()))
        elif c in binary_operations:
            stack.append(binary_operations[c](stack.pop(-2),stack.pop(-1)))
        else:
            return None
    return stack
