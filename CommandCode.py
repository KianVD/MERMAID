"""sample code for command node to listen to sensor
Later we can use c for network communication cuz its faster and lower memory then send data to a python gui"""

import socket

BUFFER_SIZE = 1024

CMDNODE_IP = "127.0.0.1"
CMDNODE_PORT = 12345

sfd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#sock bind?
sfd.bind((CMDNODE_IP, CMDNODE_PORT))

while True:
    data, addr = sfd.recvfrom(BUFFER_SIZE)
    print(f"Recieved: {data}\nFrom: {addr}")