


class EquacioPrimerGrau:

    def __init__(self, equacio):


        self.sq=equacio
        self.a=" "
        self.b=" "
        self.operador=" "
        self.c=" "


    def calcula(self):

        self.respuesta=" "
        hola=self.sq.split()
        a=hola[0]
        a=a[:-1]
        b=hola[2]
        operador=hola[1]
        c=hola[4]

        if(operador=="+"):
                respuesta=(float(c)-float(b))/float(a)


        if(operador=="-"):
                respuesta=(float(c)+float(b))/float(a)

        print("x = "+str(respuesta))




eq=EquacioPrimerGrau("20x + 30 = 70")
eq2=EquacioPrimerGrau("20x - 70 = -30")
print(eq.sq)
print(eq2.sq)
eq.calcula()
