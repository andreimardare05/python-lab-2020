import re
import socket
import urllib
import hashlib
from urllib import request
import json
import zipfile
import os


def problema2(url, cheie):
    result = json.loads(request.urlopen(url).read().decode())
    return result[cheie][-1]


print(problema2("https://pastebin.com/raw/PzM422T2", "abc"))


def problema4(lista_arhive):
    result = set()
    for item in lista_arhive:
        z = zipfile.ZipFile(item)
        for item_archive in z.infolist():
            if not item_archive.is_dir():
                result.add(os.path.basename(item_archive.filename))
        z.close()
    return list(result)


print(problema4(
    ["model_test.zip", "test_zip_p6_another_test.zip",  "test_zip_p6.zip"]))


def problema5(url):
    dictionar = json.loads(urllib.request.urlopen(url).read().decode())
    print(dictionar)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print((dictionar["ip"], dictionar["port"]))
    s.connect((dictionar["ip"], dictionar["port"]))
    text = dictionar["info"]
    s.send(text.encode())
    text = s.recv(10)
    return text.decode().count('A')


def problema1(s):
    items = re.findall(r"[a-zA-Z]+", s)
    return max(items, key=lambda x: len(x))


# print(problema5("https://pastebin.com/raw/SqhP9AAU"))
print(problema1("azi, 22ianuarie2019 dau testul 2 la python3.xx"))


def problema1_v2(s):
    result = re.findall("[02468]+", s)
    return sorted(result, reverse=True)


print(problema1_v2("azi, 22ianuarie2019 dau testul 2 la python3.xx"))


def problema3(path):
    result = {}
    for root, dirs, files in os.walk(path, topdown=True):
        for fn in files:
            result.setdefault.md5(fn.encode().hexdigest(),
                                  os.path.getsize(os.path.join(root, fn)))
    return result


def problema1(my_str):
    return re.sub("([a-z])([A-Z])", r"\1_\2", my_str).lower()


print(problema1("UpperCamelCase"))
