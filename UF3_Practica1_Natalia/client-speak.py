# Echo client program
import socket

HOST = 'localhost'    # The remote host
PORT = 50007              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    print("Introdueix una paraula")
    enviar=raw_input()
    s.sendto(enviar,((HOST,PORT)))
    if enviar=="Bye":
        break

s.close()
