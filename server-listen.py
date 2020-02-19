# Echo server program
import socket
import time
import threading

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50008              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST,PORT))
s.listen(3)
#conn2,addr2= s.accept()

"""print("connectat"+str(addr))
print("conectat"+str(addr2))
"""

nomsConexions=[]

def acceptar():
    while True:
        nomsConexions.append(s.accept())

        re2=threading.Thread(target=recive,args=(nomsConexions[-1][0],))
        re2.deamon=True
        re2.start()


def recive(conn):
    while True:
        n= conn.recv(1024)

        for x in nomsConexions:

            if x[0]!=conn:
                x[0].sendall(n)







    #    print n
    #    nomsConexions.sendall(n)
        #conn.sendall(n)

"""
def enviar(conn,conn2):
    while True:
        enviat2 = raw_input()
        enviat3 = raw_input()
        conn.sendall(enviat2)
        conn2.sendall(enviat3)



def rebre(conn,conn2):
    while True:
        t=conn.recv(1024)
        print t
        conn.sendall(t)

        if t == "Bye":
            break

def rebre2(conn,conn2):
    while True:
        t2=conn2.recv(1024)
        print t2
        conn2.sendall(t2)

        if t2 == "Bye":
            break

"""




t= threading.Thread(target=acceptar)
t.start()
t.join()



#enviarSer=threading.Thread(target=enviar,args=(conn,conn2,))
#enviarSer.daemon = True
#enviarSer.start()
"""
rebreSer2 = threading.Thread(target=rebre,args=(conn,conn2,))
rebreSer2.start()

rebreSer = threading.Thread(target=rebre,args=(conn,conn2,))
rebreSer.start()

rebreSer2.join()
rebreSer.join()

acceptar = threading.Thread(target=rebre)
acceptar.start()

acceptar.join()
"""

s.close()
