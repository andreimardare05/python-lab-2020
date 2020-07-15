import socket
import sys

ip=sys.argv[1]
port = int(sys.argv[2])
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((ip,port))
s.close()
