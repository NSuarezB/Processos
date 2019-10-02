


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
        a=a[1-1]
        b=hola[2]
        operador=hola[1]
        c=hola[4]

        if(operador=="+"):
                respuesta=(int(c)-int(b))/int(a)


        if(operador=="-"):
                respuesta= (int(c)+int(b))/int(a)

        print("x = "+str(respuesta))




eq=EquacioPrimerGrau("2x + 3 = 7")
print(eq.sq)
eq.calcula()
