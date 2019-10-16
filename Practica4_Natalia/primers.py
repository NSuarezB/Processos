# -*- coding: utf-8 -*-
import sys

# Calcula i retorna els n numeros primers entre 0 i 994


class llista_primers:

    """

    >>> llista_primers(3).l
    [2,3,5]

    >>> llista_primers(5).l
    [2,3,5,7,11]

    >>> llista_primers(1).l
    [2]

    """
    def __init__(self, n):
        """ n = arg
        inicialitza llista
        """
        self.n = n
        self.llista = []
        self.busca()

    def busca(self):
        if (len(self.llista) == 0):
        # llista[0]==2 -- Sempre
            self.llista.append(2)
            self.busca()

            """ la funcio s'acaba quan llista length==n """
        elif (len(self.llista) < self.n):
            trobat = False
            # seguent==llista[ultim valor de la llista]+1
            seguent = self.llista[-1]+1
            """ Si seguent%i==0 seguent++.
            El for es "reinicia" amb el break
             llista=llista+seguent """
            while not trobat:
                for i in self.llista:
                    if seguent%i == 0:
                        seguent += 1
                        trobat = False
                        break
                    else:
                        trobat = True
            self.llista.append(seguent)
            """ cridem constantment la funcio sense destinció
             per comprovar si s'ha acabat"""
            self.busca()


if __name__ == '__main__':
    import doctest
    doctest.testfile("doc.html")
    """     Mostra llista, i demana un argument n     """
    l = llista_primers(int(sys.argv[1]))
    print l.llista
