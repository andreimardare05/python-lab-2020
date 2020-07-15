import socket
import sys

ip="127.0.0.1"
port = int(1234)
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect((ip,port))

s.send('10|20|30|40|'.encode())
import time
time.sleep(1)
s.send(".".encode())

print(s.recv(100).decode())
s.close()
