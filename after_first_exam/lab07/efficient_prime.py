def efficient_prime(number):
    if number < 2:
        return False
    if number % 2 == 0 and number != 2:
        return False
    import math
    radical = math.sqrt(number)
    d = 3
    while d <= radical:
        if number % d == 0:
            return False
        d += 2
    return True


def ineficient_prime(number):
    d = 2
    while d <= number/2:
        if number % d == 0:
            return False
        d += 1
    return True


def test_function_prime(number):
    import datetime as datetime
    import time

    start = time.perf_counter()
    efficient_prime(number)
    finish = time.perf_counter()

    difference1 = (finish - start)
    print(finish-start)

    start = time.perf_counter() 
    ineficient_prime(number)
    finish = time.perf_counter() 

    difference2 = (finish - start)

    if (difference1 < difference2):
        print(f"The winner is the first function : {difference1}")
    else: 
        print(f"The winner is the second function : {difference2}")
    
test_function_prime(312)

