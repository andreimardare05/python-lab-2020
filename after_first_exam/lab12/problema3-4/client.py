import urllib
from urllib import request
import re

url = r"http://127.0.0.1:4200"

try:
    response = urllib.request.urlopen(url).read().decode()

    result = re.findall(r"(\w+)\.py</a></li>",response)
    
    print(result)

except Exception as e:
    print("Error -> ",e)

