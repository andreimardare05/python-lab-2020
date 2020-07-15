def problema1(matrix):
    result = 0
    for i in range(0, len(matrix)):
      result += matrix[i][i]
    return result


def problema2(my_list, x):
    return sorted(my_list, key = lambda item: item %(10)**x)


def problema3(my_list):
    info = dict()
    for item in my_list:
        if info.get(item[0]) is None:
            info.setdefault(item[0], (1, item[1]))
        else:
            info[item[0]] = (info[item[0]][0] + 1, info[item[0]][1] + item[1])
    max_town = ''
    max_count = 0
    for key,value in info.items():
        if value[0] > max_count:
            max_town = key
            max_count = value[0]
    return (max_town, info[max_town][1])


def problema4(my_list):
    for item in my_list:
        if type(item) is list:
            return 1+problema4(item)
    return 0


def problema5(text, mapping):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    mapping = list(mapping)
    text = list(text)
    for index in range(0,len(text)):
        text[index] = mapping[alphabet.index(text[index])]
        character = mapping[-1]
        mapping = mapping[:-1]
        mapping.insert(0,character)
    return ''.join(text)
        



# print(problema1([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
# print(problema2([2343, 546, 9911, 6723],2))
# print(problema3([('iasi', 420)]))
# print(problema4([(1, 2), [{'2': 3}, [2, [3, [4, [[[]]]]]]]]))
# print(problema5("testlapython","hvrlpwkzmgsyobxidfecantjuq"))