import datetime
import time
from multiprocessing import Process

def t(s):

    while (True):
        time.sleep(s)
        print(datetime.datetime.now().time())

def main():
    m=0
    p=Process(target=t,args=(1,))
    p.start()
    while(m<10):
        time.sleep(0.5)
        print(p.pid)
        m=m+1
    p.terminate()
    print("fi")
__name__ == '__main__'

main()
