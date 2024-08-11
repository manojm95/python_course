def add(x, y):
    sum = x + y
    return sum


def sub(x, y):
    diff = x - y
    return diff


def mul(x, y):
    product = x * y
    return product


def division(x, y):
    div = x / y
    return div


operator_dict = {
    'add': add,
    'sub': sub,
    'mul': mul,
    'div': division
}


def calculator(operator, x, y):
    if operator == 'add':
        answer = add(x, y)
    elif operator == 'sub':
        answer = sub(x, y)
    elif operator == 'mul':
        answer = mul(x, y)
    elif operator == 'div':
        answer = division(x, y)
    # answer = operator_dict[operator](x, y)
    print(answer)


calculator('mul', 2, 3)
