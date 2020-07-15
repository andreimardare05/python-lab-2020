import os
import json
from urllib import request
import urllib
import re
import hashlib


def problema0(a, b):
    result = 0
    for index in range(a, b):
        result += index
    return result


print(problema0(1, 10))


def problema1(my_str):
    index = 0
    result = my_str[index].lower()
    for index in range(1, len(my_str)):
        if my_str[index] == my_str[index].upper():
            result = result + '_' + my_str[index].lower()
        else:
            result = result + my_str[index]
    return result


print(problema1("CamelCase"))


def problema2(my_list):
    distincte = set(my_list)
    result = []
    for item in distincte:
        if my_list.count(item) % 2:
            result.append(item)
    return result


print(problema2(my_list=[1, 2, 3, 4, 1, 2, 2, 3, 4, 4, 4, 5]))


def problema3(my_list):
    result = {}
    for item in my_list:
        if re.search("[0-9]{5}", item):
            result.setdefault(hashlib.md5(item.encode()).hexdigest(), item)
    return result


print(problema3(my_list=["ss12345", "54321cba",
                         "a11111a", "2222a2", "a", "123456"]))


def problema4(my_url):
    result = {}
    result = json.loads(request.urlopen(my_url).read().decode())
    res = [result["data"]]
    while "next" in result.keys():
        result = json.loads(request.urlopen(result["next"]).read().decode())
        res.append(result["data"])
    return res


print(problema4("https://pastebin.com/raw/auJgyakH"))


def problema6(**args):
    if "my_file" in args.keys():
        dictionar = json.load(open(args["my_file"]))
        result = []
        for item in os.listdir(dictionar["path"]):
            if os.path.isfile(os.path.join(dictionar["path"],item)):
                print(item, hashlib.sha256(open(os.path.join(dictionar["path"],item),"rb").read()).hexdigest())
                if hashlib.sha256(open(os.path.join(dictionar["path"],item),"rb").read()).hexdigest() == dictionar["sha"]:
                    result.append(item)
    elif "my_folder" in args.keys():
        dicthash = dict()
        for root, dirs, files in os.walk(args["my_folder"]):
            for filename in files:
                path_file = (root + '/' + filename)
                content = open(path_file, "rb").read()
                cheie = hashlib.sha256(content).hexdigest()
                if cheie not in dicthash.keys():
                    dicthash.setdefault(cheie, [path_file])
                else:
                    dicthash[cheie].append(path_file)
        maxcount = 0
        maxvalue = 0
        for value in dicthash.values():
            if len(value) > maxcount:
                maxcount = len(value)
                maxvalue = value
        result = maxvalue
    return result

print(problema6(my_file ="test_zip_p6/caz1/a.json"))