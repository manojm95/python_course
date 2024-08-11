def square(x):
    return x*x


def cube(x):
    return x*x*x


def do_something(x):
    sq = square(x)
    if sq == 4:
        return cube(x)
    else:
        return None


print(do_something(2))

# == equal to
# >= gte
# <= lte
# >
# <


