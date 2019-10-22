# -*- coding: utf-8 -*-
import sys


class llista_primers:

    """
    Calcula els n numeros primers entre 2 i 994


    Tests:

    >>> llista_primers(3).llista
    [2, 3, 5]

    >>> llista_primers(5).llista
    [2, 3, 5, 7, 11]

    >>> llista_primers(1).llista
    [2]

    """
    def __init__(self, n):
        """
        ___n___ = numeros mostrats.
        ___llista___= array buida.

        S'activa la funcio busca
        """
        self.n = n
        self.llista = []
        self.busca()

    def busca(self):
        """
        ################################
         Aquesta es la funció principal
        ################################

        ___llista___ Sempre començara per 2, ja que sempre comença buit.


        if ___llista.length___==0 ;  then __llista__=llista[2];

        else ; comença la busqueda de nombres primers

        !!! la funcio s'acaba quan llista length==n !!!

        ___seguent___==___llista___[ultim valor de la llista]+1;

        Es comprova si es numero primer amb els numeros afegits a l'array
        Si seguent%i==0 seguent++;

        El for es "reinicia" amb el break
         ___llista___=llista.add(___seguent___)


        Cridem constantment la funcio sense destinció
          per comprovar si s'ha acabat

        """

        if (len(self.llista) == 0):
        # llista[0]==2 -- Sempre
            self.llista.append(2)
            self.busca()

        elif (len(self.llista) < self.n):
            trobat = False
            seguent = self.llista[-1]+1

            while not trobat:
                for i in self.llista:
                    if seguent%i == 0:
                        seguent += 1
                        trobat = False
                        break
                    else:
                        trobat = True
            self.llista.append(seguent)

            self.busca()


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    #l = llista_primers(int(sys.argv[1]))
    #print l.llista
