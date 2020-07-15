from http.server import HTTPServer
from http.server import SimpleHTTPRequestHandler

httpd = HTTPServer(("127.0.0.1",4200), SimpleHTTPRequestHandler)
httpd.serve_forever()