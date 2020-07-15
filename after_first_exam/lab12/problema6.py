import urllib
from urllib import request
import hashlib

url = "https://www.crtsiasi.ro"

context = urllib.request.urlopen(url)

info = f"{context.getcode()}, {context.info()['Content-Length']}, {context.info()['Content-Type']}"

with context as r:
    text = r.read(1000)
    while text:
        info = info + ', ' + hashlib.md5(text).hexdigest()
        text = r.read(1000)

print(info)