


class EquacioPrimerGrau:

    def __init__(self, equacio):


        self.sq=equacio
        self.a=" "
        self.b=" "
        self.operador=" "
        self.c=" "


    def calcula(self):
        try:

            self.respuesta=" "
            hola=self.sq.split()
            self.a=hola[0]
            self.a=self.a[:-1]
            self.b=hola[2]
            try:
                self.b=float(self.b)
            except:
                return ("l'equacio no segueix el format: ax + b = c")

            self.operador=hola[1]
            self.c=hola[4]

        except:
            return ("l'equacio no segueix el format: ax + b = c")


        #if(self.b[1]=="x"):
        #    self.respuesta=str("l'equacio no segueix el format: ax + b = c")
        #    """

        if(self.operador=="+"):
                self.respuesta=(float(self.c)-float(self.b))/float(self.a)
        elif(self.operador=="-"):
                self.respuesta=(float(self.c)+float(self.b))/float(self.a)
        else:
            return ("Operador no valid: "+self.operador)

        return self.respuesta










eq=EquacioPrimerGrau("2x - p = 7")

print(eq.calcula())
