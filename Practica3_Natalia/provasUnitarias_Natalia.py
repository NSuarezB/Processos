
import unittest
from equacio1_1Grau_Natalia import EquacioPrimerGrau

class EquacioPrimerGrau_test(unittest.TestCase):

    def test_positiu(self):
        eq = EquacioPrimerGrau("2x + 3 = 7")
        self.assertEqual(eq.calcula(),2)

    def testincorrecte(self):
        eq = EquacioPrimerGrau("2x / 3 = 7")
        self.assertEqual(eq.calcula(),"Operador no valid: "+eq.operador)
        self.assertIsInstance(eq.operador, basestring)

    def test_negatiu(self):
        eq = EquacioPrimerGrau("2x - 3 = 7")
        self.assertEqual(eq.calcula(),5)

    def test_float(self):
        eq = EquacioPrimerGrau("2.3x - 8.4 = 9.8")
        self.assertEqual(eq.calcula(),7.913043478260872)

    def test_no_conte(self):
        eq = EquacioPrimerGrau("2x - p = 7")
        self.assertEqual(eq.calcula(),"l'equacio no segueix el format: ax + b = c")

    def test_fromat_erroni(self):
        eq = EquacioPrimerGrau("3 - 2x = 7")
        self.assertEqual(eq.calcula(),"l'equacio no segueix el format: ax + b = c")



if __name__ == '__main__':
    unittest.main()
