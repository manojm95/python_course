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
    'div': division,
    "div_float": division
}


# operator can be add, sub, mul or div
def calculator(operator, inputs):
    # if operator not in ['add', 'sub', 'mul', 'div']:
    #     raise Exception
    if operator not in operator_dict.keys():
        raise Exception
    x = inputs[0]
    y = inputs[1]
    answer = operator_dict[operator](x, y)
    print(answer)


calculator('add1', [2, 3])
