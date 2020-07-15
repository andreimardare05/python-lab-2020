import socket
import sys

ip="127.0.0.1"
port = int(1235)
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect((ip,port))

fd = open("dict.json","r")
content = fd.read()
import json
input_dict = json.loads(content)

s.send(json.dumps(input_dict).encode())

s.send("glossary".encode())

print(s.recv(1000).decode())
s.close()
