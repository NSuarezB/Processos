# Echo server program
import socket
import time

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind((HOST,PORT))

while(True):
    COSA=s.recv(1024)
    print(COSA)

    if COSA=="Bye":
        print("El port es tencara")
        time.sleep(1)

        break


s.close()
