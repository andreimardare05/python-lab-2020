def problema1(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    result = [1, 1]
    for index in range(2, n, 1):
        result.append(result[index-1]+result[index-2])
    return result


def prime(number):
    import math
    if number < 2:
        return 0
    if number % 2 == 0 and number != 2:
        return 0
    d = 3
    radical = math.sqrt(number)
    while d <= radical:
        if number % d == 0:
            return False
        d += 2
    return True


def problema2(input_numbers):
    return [item for item in input_numbers if prime(item)]


def problema4(a, b):
    set_a = set(a)
    set_b = set(b)
    return (list(set_a.intersection(set_b)), list(set_a | set_b), list(set_a - set_b), list(set_b - set_a))

# def problema5(x, k):
#     index = 0
#     for index in range(0,len(x)-k+1)
#         for another_index in range(0, k):


def problema6(*args, x=1):
    all_lists = []
    for item in args:
        all_lists.extend(item)
    all_different_items = set(all_lists)
    return [item for item in all_different_items if all_lists.count(item) == x]


def problema7(*args, flag=True, x=2):
    if flag:
        return [[char for char in text if ord(char) % x == 0] for text in args]
    else:
        return [[char for char in text if ord(char) % x == 1] for text in args]


def problema8(args):
    size = max([len(x) for x in args])
    for index in range(0, len(args)):
        if len(args[index]) < size:
            for another_index in range(0, size-len(args[index])):
                args[index].append(None)
                another_index = another_index
    return list(zip(*args))


def problema9(tuples_list):
    return sorted(tuples_list, key=lambda item: item[1][2])


# print(problema1(5))
# print(problema2([5, 3, 6, 1, 4, 10, 2]))
# print(problema4([1, 2, 3], [3, 4, 5]))
# print(problema6([1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"], x=2))
# print(problema7("test", "hello", "lab002", flag=False, x=2))
# print(problema8([[1, 2, 3], [5, 6, 7], ["a", "b"]]))
# print(problema9([('abc', 'bcd'), ('abc', 'zza')]))
