def prime(number):
    import math
    if number < 2:
        return False
    if number != 2 and number % 2 == 0:
        return False
    radical = math.sqrt(number)
    d = 3
    while d < radical:
        if number % d == 0:
            return False
        d += 2
    return True


def process_item(x):
    x = x + 1
    while True:
        if prime(x):
            return x
        x = x + 1
    return x