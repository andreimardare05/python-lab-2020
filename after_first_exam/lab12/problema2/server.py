import socket
import time
import hashlib

ip = "127.0.0.1"
port = 4200
bufferSize = 1024

udpsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

udpsock.bind((ip,port))

print("Server up and running!")

while True:
    bytesAddressPair = udpsock.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    text = bytesAddressPair[0].decode()

    write_in_file = f'{time.strftime(r"%H:%M:%S - %d-%m-%Y",time.localtime())} - {bytesAddressPair[1][0]}, {bytesAddressPair[1][1]} - {len(text)}\nmd5 : {hashlib.md5(message).hexdigest()}\nsha256 : {hashlib.sha256(message).digest()}\n'
    print(write_in_file)
    with open("output.txt", "a") as fd:
        fd.write(write_in_file)

fd.close()