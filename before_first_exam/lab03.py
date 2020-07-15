def problema1(list_a, list_b):
    set_a = set(list_a)
    set_b = set(list_b)
    result = set()
    result.add(frozenset(set_a | set_b))
    result.add(frozenset(set_a & set_b))
    result.add(frozenset(set_a - set_b))
    result.add(frozenset(set_b - set_a))
    return result


def problema2(string):
    result = dict()
    for char in string:
        if not char in result.keys():
            result.setdefault(char, 1)
        else:
            result[char] = result[char] + 1
    return result


# def problema3(dict1, dict2):
#     if not len(dict1) == len(dict2):
#         return False
#     if not type(dict1) == type(dict2):
#         return False
#     else:
#         if type(dict1) == dict:
#             for key_dict1 in dict1.keys():
#                 for key_dict2 in dict2.key():
#                     if key_dict1 == key_dict2:
#                         if type(key_dict1) == type(key_dict2):
#                             return problema3(dict1[key_dict1], dict2[key_dict2])
#         elif type(dict1) == list or type(dict1) == set:
#             for item in dict1:
#     return True


def problema4(tag, content, **kwargs):
    result = f'<{tag}'
    for key, value in kwargs.items():
        result = ''.join([result, f' {key}=\\"{value}"\\'])
    return ''.join([result, '> ', f'{content} </{tag}>'])


def problema5(tuples, dictionary):
    for rule in tuples:
        if rule[0] not in dictionary:
            return False
        if not dictionary[rule[0]].startswith(rule[1]) or not dictionary[rule[0]].endswith(rule[3]) or not rule[2] in dictionary[rule[0]][1:-1]:
            return False
    return True


def problema6(s):
    return len(s), 0




def problema7(a, b):
    return {
        f'{a} | {b}': a | b,
        f'{a} & {b}': a & b,
        f'{a} - {b}': a - b,
        f'{b} - {a}': b - a
        }


# print(problema1([1,2,3],[3,4,5]))
# print(problema2("Ana has apples."))
print(problema4("a", "Hello there", href=" http://python.org ", _class=" my-link "))
print(problema5({("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}, {
      "key1": "come inside, it's too cold out", "key2": "start is not  winter"}))
print(problema6({'ana', 1, 3, 'ana', 1, 1, 10}))
print(problema7({1,2,3},{3,4,5}))
