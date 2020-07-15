def problema1(tuples):
    return sorted(tuples, key=lambda item: item[1])


def problema2(tuples, first_name):
    if not len([item for item in tuples if first_name in item[1]]):
        return False
    return True


global_dict = {

    "+": lambda a, b: a + b,

    "*": lambda a, b: a * b,

    "/": lambda a, b: a / b,

    "%": lambda a, b: a % b

}


def problema3(operator, a, b):
    return global_dict[operator](a, b)


global_fdict = {
    "print_all": lambda *a, **k: print(a, k),
    "print_args_commas": lambda *a, **k: print(a, k, sep=", "),
    "print_only_args": lambda *a, **k: print(a),
    "print_only_kwargs": lambda *a, **k: print(k)
}


def problema4(operation, *a, **k):
    return global_fdict[operation](a, k)


def problema5(*args):
    result = {}
    for dictionary in args:
        for key, value in dictionary.items():
            if not key in result:
                result[key] = value
            else:
                if not type(result[key]) is list:
                    result[key] = [result[key], value]
                else:
                    result[key].append(value)
    return result




def problema6(argument, separator=""):
    def do(argument, string="", separator="-"):
        for key, value in argument.items():
            if type(argument[key]) is dict:
                do(argument[key], f"{string}'{key}' {separator} ","-")
            else:
                print(string + f"'{key}' {separator} {value}")
    do(argument, "", "-")


print(problema1([('Miruna', 'Zota'), ('Ioana', 'Bujder')]))
print(problema2([('Miruna', 'Zota'), ('Ioana', 'Bujder')], 'Bujder I.'))
print(problema3('+', 10, 20))
print(problema4('print_all', [1, 2, 3], x=3))
print(problema5({"a": 10}, {"b": 20, "c": 5},
                {"a": 30, "b": 50}, {"c": 5, "b": 60}))
problema6({'a': 1, 'b': {'c': 3, 'd': {'e': 5, 'f': 6}}}, "")
