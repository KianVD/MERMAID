"""Sample code for sending several udp messages to a command node"""

import socket

#command node IP
CMDNODE_IP = "127.0.0.1"
CMDNODE_PORT = 12345

sfd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for i in range(100):
    sfd.sendto(f"Yo{i}", (CMDNODE_IP, CMDNODE_PORT))

sfd.close()