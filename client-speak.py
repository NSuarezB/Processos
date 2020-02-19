# Echo client program
import socket
import threading


HOST = 'localhost'        # The remote host
PORT = 50008              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((HOST,PORT))


#enviar=raw_input()

def enviar(s):
    while True:
        n = raw_input("Introdueix una paraula")
        s.sendall(n)
        if n == "Bye":
            break

def rebre(s):
    while True:
        m = s.recv(1024)
        print m

        if m == "Bye":
            break

enviarCli = threading.Thread(target=enviar, args=(s,))
enviarCli.deamon = True
enviarCli.start()

rebreCli = threading.Thread(target=rebre, args=(s,))
rebreCli.start()

rebreCli.join()

s.close()
