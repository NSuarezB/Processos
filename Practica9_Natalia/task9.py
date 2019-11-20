#-*- coding: utf8 -*-
#4523

# 40 / 2 = 20
# 40 / 4 = 10
from multiprocessing import Pool
from datetime import datetime

def primers(num):
    for i in range(2, num/2):
        if num % i == 0:
            return False
        else:
            pass
    return True

if __name__ == '__main__':
    # Aqui li poses els processos el numero es els porcessos que fa
    pool = Pool(processes=4)
    l = range(4000000, 4000100)#[45445535, 56534563, 43566487, 43635453, 52346557, 53454433, 43546453, 26847357, 54577647]
    start = datetime.now()

    for i in pool.map(primers,l):
        for j in l:

            print i,j
    print datetime.now() - start


    # Surt a compte si tens un gran rang de numeros, sino la diferencia es molt petita
    # El mes rapid es el map

    #1 4.982249
    #2 5.085796
    #3 5.076574
    #4 5.049323

    #4.968676

    #4 5.101780
    #1 6.833429
