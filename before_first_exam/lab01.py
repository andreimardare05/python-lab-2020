def problema1(a, b):
    while b:
        c = a % b
        a = b
        b = c
    return a



def problema2(text):
    result = 0
    for letter in text:
        if letter.lower() in "aeiou":
            result = result+1
    return result


def problema2_optimisation(text):
    vowels = "aeiou"
    return len([letter for letter in text if letter.lower() in vowels])


def problema3(string, substring):
    return string.count(substring)


def problema3_alternative(string, substring):
    import re
    return len(re.findall(substring, string))


def problema4(string):
    result = [string[0].lower()]
    for c in string[1:]:
        if c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            result.append('_')
            result.append(c.lower())
        else:
            result.append(c)
    return ''.join(result)


def problema5(matrix):
    m = len(matrix)
    n = len(matrix[0])
    k = 0  # row
    l = 0  # column
    while k < m and l < n:
        for i in range(l, n):
            print(matrix[k][i])
        k += 1
        for i in range(k, m):
            print(matrix[i][n-1])
        n -= 1
        if k < m:
            for i in range(n-1, l-1, -1):
                print(matrix[m-1][i])
            m -= 1
        if l < n:
            for i in range(m-1, k-1, -1):
                print(matrix[i][l])
            l += 1


# print(problema1(15, 3))
# print(problema2("Ioana."))
# print(problema3("Lorem ipsuemLoremIpsem", "em"))
# print(problema4('UpperCamelCanse'))
# problema5([[1, 2, 3, 4], [12, 13, 14, 5],
#             [11, 16, 15, 6], [10, 9, 8, 7]]))
