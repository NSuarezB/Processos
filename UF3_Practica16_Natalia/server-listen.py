# Echo server program
import socket
import time
import threading

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50008              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST,PORT))
s.listen(1)
conn,addr= s.accept()

print("connectat"+str(addr))


def enviar(conn):
    while True:
        enviat2 = raw_input()
        conn.sendall(enviat2)

        if enviat2 == "Bye":
            break


def rebre(conn):
    while True:
        t=conn.recv(1024)
        print t

        if t == "Bye":
            conn.sendall(t)
            break

enviarSer=threading.Thread(target=enviar,args=(conn,))
enviarSer.daemon = True
enviarSer.start()

rebreSer = threading.Thread(target=rebre,args=(conn,))
rebreSer.start()

rebreSer.join()

s.close()
