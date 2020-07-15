def problema2(*args, **kwargs):
    result = 0
    for value in kwargs.values():
        result += value
    return result


problema2_anonymous = lambda *args, **kwargs: sum(kwargs.values())

print(problema2(1, 2, c=3, d=4))
print(problema2_anonymous(1, 2, c=3, d=4))


def problema3(string):
    result = []
    for char in string:
        if char.lower() in "aeiou":
            result.append(char)
    return result


def problema3_anonymous(string): return [
    char for char in string if char.lower() in "aeiou"]


def problema3_filter(string):
    return list(filter(lambda x: x.lower() in "aeiou", string))


print(problema3("Programming in Python is fun"))
print(problema3_anonymous("Programming in Python is fun."))
print(problema3_filter("Programming in Python is fun."))


def problema4(*args, **kwargs):
    result = []
    for item in args:
        if type(item) is dict:
            if len(item.keys()) >= 2:
                for key in item.keys():
                    print(key)
                    if len(str(key)) >= 3:
                        result.append(item)
                        break
    for item in kwargs.values():
        if type(item) is dict:
            if len(item.keys()) >= 2:
                for key in item.keys():
                    print(key)
                    if len(str(key)) >= 3:
                        result.append(item)
                        break
    return result


print(problema4({1: 2, 3: 4, 5: 6},
                {'a': 5, 'b': 7, 'c': 'e'},
                {2: 3},
                [1, 2, 3],
                {'abc': 4, 'def': 5},
                3764,
                dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'},
                test={1: 1, 'test': True}))


def problema5(input_list):
    def check(item): return type(item) == int or type(
        item) == float or type(item) == complex
    result = []
    for item in input_list:
        if check(item):
            result.append(item)
        elif type(item) == dict:
            for key in item.keys():
                if check(key):
                    result.append(key)
        elif type(item) == list or type(item) == set or type(item) == frozenset:
            for element in item:
                if check(element):
                    result.append(element)
    return list(set(result))


print(problema5([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]))


def problema6(list1, list2):
    result = []
    for item in zip(list1, list2):
        result.append((item[0][1] - item[1][1], item[1][0] - item[0]
                       [0], item[0][0]*item[1][1] - item[1][0]*item[0][1]))
    return result
    # a = (yA−yB), b = (xB−xA), c = xAyB−xByA


def problema6_map(list1, list2):
    return list(map(lambda item: (item[0][1] - item[1][1], item[1][0] - item[0][0], item[0][0]*item[1][1] - item[1][0]*item[0][1]), zip(list1, list2)))


print(problema6([(1, 2), (7, 0)], [(5, 6), (9, 15)]))
print(problema6_map([(1, 2), (7, 0)], [(5, 6), (9, 15)]))


def problema7(input_list):
    odd_numbers = list(filter(lambda x: not x % 2 == 0, input_list))
    even_numbers = list(filter(lambda x: x % 2 == 0, input_list))
    return list(zip(even_numbers, odd_numbers))


print(problema7([1, 3, 5, 2, 8, 7, 4, 10, 9, 2]))


def generate_fibonnaci(n):
    result = []
    if n == 0:
        return result
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    if n > 2:
        result = [1, 1]
        for index in range(2, n+1):
            result.append(result[index-1] + result[index-2])
    return result

    
def sum_digits(x):
    return sum(map(int, str(x)))

def problema8(**kwargs):
    numbers = generate_fibonnaci(1000)
    if "filters" in list(kwargs.keys()):
        for filter_apply in kwargs["filters"]:
            numbers = list(filter(filter_apply,numbers))
    if "offset" in list(kwargs.keys()):
        numbers = numbers[kwargs["offset"]-1:]
    if "limit" in list(kwargs.keys()):
        numbers = numbers[:kwargs["limit"]]
    return numbers

print(problema8(filters=[lambda item: item % 2 == 0, lambda item: item == 2 or 4 <= sum_digits(item) <= 20],limit=2,offset=2))
