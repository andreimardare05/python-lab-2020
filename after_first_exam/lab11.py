import re


def problema1(text):
    return re.findall('\\w+', text)


print(problema1('Lorem ipsum. This is an demo1 text!'))


def problema2(regex, text, x):
    result = re.findall(regex, text)
    return list(filter(lambda item: len(item) == x, result))


print(problema2('\\w+', 'Lorem ipsum. This is an demo1 text!', 4))


def problema3(text, expressions):
    result = set()
    for exp in expressions:
        result = result | set(re.findall(exp, text))
    return list(result)


print(problema3('Lorem ipsum. This is an demo1 text! 123', ['\\w+', '\\W+']))


def problema4(path, attrs):
    exp = '<(\\w+)'
    for key, value in attrs.items():
        exp = exp + f'[ ]+({key}="{value}")'
    exp = exp + '>'
    pattern = re.compile(exp)
    fd = open(path, "r")
    text = fd.read()
    m = pattern.findall(text)
    return list(map(lambda el: el[0], m))


def problema6(text):
    exp = r"voices(\w+)voices"
    pattern = re.compile(exp)
    for m in pattern.finditer(text):
        start = int(m.start())
        end = int(m.end())
        replacement = "voices"
        for index in range(start+6, end - 6):
            if not index % 2:
                replacement = replacement + "*"
            else:
                replacement = replacement + text[index]
        replacement = replacement + "voices"
        text = text[:start] + replacement + text[end:]
    return text


print(problema4("book.xml", {"class": "url",
                             "name": "url-form", "date-id": "item"}))

print(problema6("voicesWintervoices is coming to voicesWesterosvoices"))


def problema7(cnp):
    exp = r"^([1-8]([1-9][0-9])(0[0-9]|11|12)(0[1-9]|[1-2][0-9]|30|31)(0[1-9]|[1-4][0-9]|50|51|52)[0-9]{4})$"
    pattern = re.compile(exp)
    if pattern.match(cnp):
        return True
    else:
        return False


def problema8(path, regexp):
    import os
    for root, dirs, files in os.walk(path):
        for file_name in files:
            if re.compile(regexp).match(file_name):
                path_file = os.path.join(root, file_name)
                fd = open(path_file, "r")
                content = fd.read()
                fd.close()
                if re.compile(regexp).search(content):
                    file_name = ">>" + file_name
                    print(file_name)
                else:
                    print(file_name)


print(problema7("1900205304525"))

problema8("test_folder", "dat")


def problema9(path):
    import os
    import hashlib
    import time

    result = []
    for root, dirs, files in os.walk(path):
        for file_name in files:
            path_file = os.path.join(root, file_name)
            fd = open(path_file, "rb")
            content = fd.read()
            statinfo = os.stat(path_file)
            fd.close()
            result.append({
                "file_name": file_name,
                "md_5": hashlib.md5(content).hexdigest(),
                "sha_256": hashlib.sha256(content).hexdigest(),
                "size_file": statinfo.st_size,
                "time_created": time.ctime(statinfo.st_ctime),
                "abs_path": os.path.abspath(path_file)
            })
    return result


def problema10(path):
    import hashlib
    import os
    md5_dict = dict()
    for root, dirs, files in os.walk(path):
        for file_name in files:
            fd = open(os.path.join(root, file_name), "rb")
            hash_file = hashlib.md5(fd.read()).hexdigest()
            if hash_file in md5_dict:
                md5_dict[hash_file].append(file_name)
            else:
                md5_dict[hash_file] = [file_name]

    print(md5_dict)
    return [item[0] for item in md5_dict.values() if len(item) > 1]


# print(problema9("test_folder"))
# print(problema10("test_folder"))
