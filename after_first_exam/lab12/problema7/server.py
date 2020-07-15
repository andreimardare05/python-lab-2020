import socket
import sys
import time
import re

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 12345))
s.listen(1)
(connection, address) = s.accept()
print(f"An client has connected on \
{time.ctime()} with IP: {address[0]} PORT: {address[1]}")
result = 0
while True:
    data = connection.recv(32).decode("UTF-8")
    if data:
        connection.send("AnaAremere".encode())
        break
connection.close()
print("Server closed!")
