def problema1(s):
    import re
    return sorted(re.findall(r"\w+", s))


def problema2(s, url):
    import re
    pattern = re.compile(f"https://(\w.)({s}.)")
    if pattern.search(url):
        return True
    else:
        return False


def problema3(path):
    import hashlib
    import os
    result = []
    for root, dirs, files in os.walk(path):
        for file_name in files:
            path_file = os.path.join(root, file_name)
            fd = open(path_file, "rb")
            result.append(hashlib.sha256(fd.read()).hexdigest())
            fd.close()
    return sorted(result)


def problema4():
    import os
    import sys
    result = []
    for file_name in os.listdir(sys.argv[1]):
        path_file = os.path.join(sys.argv[1], file_name)
        if os.path.isfile(path_file):
            result.append(os.path.getsize(path_file))
    result = set(result)
    return list(sorted(result))


def problema5(cod):
    import re
    operatii = {
        "egal": lambda x, y:  y,
        "plus": lambda x, y:  x+y,
        "minus": lambda x, y:  x-y,
        "impartit": lambda x, y:  x/y,
        "inmultit": lambda x, y:  x*y,
    }
    instructiuni = re.split(r'\n', cod)
    pattern = re.compile(r'(\w+) (\w+) (\d+)')
    m = pattern.match(instructiuni[0])
    result = int(m.group(3))
    for index in range(1, len(instructiuni)):
        m = pattern.match(instructiuni[index])
        result = operatii[m.group(2)](result, int(m.group(3)))
    return int(result)


def problema7():
    import sys
    import time
    import datetime
    dates = sys.argv[1:]
    result = [datetime.datetime.strptime(
        item, r'%m/%d/%Y_%H.%M.%S') for item in dates]
    date1 = max(result)
    date2 = min(result)
    return (sorted([datetime.datetime.strftime(item, r'%Y-%m-%d %H:%M:%S') for item in result], reverse=True), int((date1-date2).total_seconds()))


def parse(path):
    import re
    pattern = re.compile(
        r"^((([0-9])|([1-9][0-9])|(1[0-9]{2})|(2[0-4][0-9])|(25[0-5]))\.){3}(([0-9])|([1-9][0-9])|(1[0-9]{2})|(2[0-4][0-9])|(25[0-5])) ")
    fd = open(path, "r")
    result = list()
    text = fd.readline()
    while text:
        m = pattern.match(text)
        if m:
            ip = m.group(0)
            result.append(str.strip(ip))
        text = fd.readline()
    return result


def problema9(path):
    import os
    result = []
    if os.path.isdir(path):
        for root, dirs, files in os.walk(path):
            for file_name in files:
                if file_name == "access.log":
                    path_file = os.path.join(root, file_name)
                    result = result + parse(path_file)
    elif os.path.isfile(path):
        result = result + parse(path)
    unique = set(result)
    result_tuple = []
    for item in unique:
        result_tuple.append((item, result.count(item)))
    result = sorted(result_tuple, key=lambda x: x[1], reverse=True)[:7]
    return list(map(lambda x: x[0], result))

# print(problema9("access.log"))


def check(path):
    import hashlib
    import re

    hash_of = {
        "md5": lambda x: hashlib.md5(x).hexdigest(),
        "sha256": lambda x: hashlib.sha256(x).hexdigest(),
        "sha512": lambda x: hashlib.sha512(x).hexdigest(),
    }

    exp_content = r"<CONTENT>(\w+)</CONTENT>"
    exp_signature_type = r"<SIGNATURE><TYPE>(\w+)</TYPE><HEXDIGEST>(\w+)</HEXDIGEST></SIGNATURE>"

    fd = open(path, "r", encoding="utf-8")
    text = fd.read()

    pattern = re.compile(exp_content)
    m = pattern.search(text)
    content = m.group(1)
    content = content.encode("utf-8")

    pattern = re.compile(exp_signature_type)
    m = pattern.search(text)
    typesig = m.group(1)
    hexsig = m.group(2)

    if hash_of[typesig](content + b"\xd0\xf3\xde\x9a\x8c\x80\x8d\xf0\x92\x94") == hexsig:
        return True
    else:
        return False


def problema10(path):
    import os

    if os.path.isfile(path):
        return check(path)

    elif os.path.isdir(path):
        result = []
        for root, dirs, files in os.walk(path):
            for file_name in files:
                if check(os.path.join(root, file_name)) == False:
                    result.append(file_name)
        return sorted(result)


def problema10(path):
    regex_content = re.compile(b"<CONTENT>(.*?)</CONTENT>", re.DOTALL)
    regex_signature_type_type = re.compile(b"<TYPE>(.*?)</TYPE>")
    regex_hexdigest = re.compile(b"<HEXDIGEST>(.*?)</HEXDIGEST>")

    def decode_hash(signature):
      if signature.upper()=='MD5':
        return hashlib.md5()
      if signature.upper()=='SHA256':
        return hashlib.sha256()
      if signature.upper() == 'SHA512':
        return hashlib.sha512()
      return hashlib.new(signature)

    def check(filex):
        with open(filex, "rb") as fd:
            allText = fd.read()
            hash_method = decode_hash(regex_signature_type_type.search(allText).group(1).decode())
            hash_method.update(regex_content.search(allText).group(1))
            hash_method.update(b"\xd0\xf3\xde\x9a\x8c\x80\x8d\xf0\x92n7\x94")
            return hash_method.hexdigest() == regex_hexdigest.search(allText).group(1).decode()


    if os.path.isfile(path):
        return check(path)

    result = []
    for root, dirs, files in os.walk(path):
        for f in files:
            if not check(os.path.join(root, f)):
                result.append(os.path.basename(f))
    result = list(sorted(result))
    return result


# print(problema10("date.xml"))
