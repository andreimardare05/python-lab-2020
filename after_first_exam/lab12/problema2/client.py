import socket
import sys

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

serverAddressPort = (sys.argv[1], int(sys.argv[2]))

client_socket.sendto(str.encode(sys.argv[3]),serverAddressPort)