import urllib
from urllib import request
import urllib.request

url = "https://www.crtsiasi.ro"

try:
    response = urllib.request.urlopen(
        url + "/pagina_contact.html").read().decode("utf-8")

    import re

    print(response)

    result = re.findall(r'<img[^>]* src=\"([^\"]*)\"[^>]*>', response)

    print(result)

    for item in result:
        response = urllib.request.urlopen(url).read().decode("utf-8")
        with urllib.request.urlopen(url + '/' + item) as response, open(item.split('/')[-1], 'wb') as out_file:
            data = response.read()
            out_file.write(data)

except Exception as e:
    print("Error -> ", e)
