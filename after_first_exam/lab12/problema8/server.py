import socket
import sys
import time
import json

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 1235))
s.listen(1)
(connection, address) = s.accept()
print(f"An client has connected on \
{time.ctime()} with IP: {address[0]} PORT: {address[1]}")
key = None
while True:
    data = connection.recv(1000).decode("UTF-8")
    try:
        input_dict = json.loads(data)
    except:
        if data:
            key = data
            print(input_dict,key)
            if key in input_dict.keys():
                connection.send(str(input_dict[key]).encode())
                break
            else:
                break
        else:
            break


connection.close()
print("Server closed!")
