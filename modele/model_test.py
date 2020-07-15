import socket
import zipfile
import os
import hashlib
import re
import urllib
from urllib import request


def problema1(s):
    return sorted(re.findall(r'(\w+)', s))


def problema2(s, url):
    if re.search(s, request.urlopen(url).read().decode("UTF-8")):
        return True
    return False


def problema3(path):
    result = []
    if os.path.isdir(path):
        for file_name in os.listdir(path):
            path_file = os.path.join(path, file_name)
            if os.path.isfile(path_file):
                result.append(hashlib.md5(
                    open(path_file, "rb").read()).hexdigest())
    return sorted(result)


def problema4(path):
    result = []
    z = zipfile.ZipFile(path)
    for i in z.infolist():
        if 1000 < int(i.compress_size):
            result.append(i.filename.split('/')[-1])
    z.close()
    return sorted(result)


print(problema4("after_first_exam.zip"))


def problema5(host, port, text):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect((host, port))

    s.send(text.encode())

    text = s.recv(32)

    s.send(hashlib.sha256(text).hexdigest().encode())

    return s.recv(32).decode()