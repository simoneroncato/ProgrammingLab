import unittest
import my_math

class TestMath(unittest.TestCase):
    def test_divisori(self):
        prova1 = my_math.TrovaDivisori(6)
        self.assertEqual(prova1.trova_divisori(), [1, 2, 3, 6])
        prova2 = my_math.TrovaDivisori(13)
        self.assertEqual(prova2.trova_divisori(), [1, 13])

    def test_div_comuni(self):
        prova1 = my_math.TrovaDivisoriComuni(6, 9)
        self.assertEqual(prova1.trova_divisori_comuni(), [1, 3])
        prova2 = my_math.TrovaDivisoriComuni(5, 21)
        self.assertEqual(prova2.trova_divisori_comuni(), [1])

    def test_mcd(self):
        prova1 = my_math.TrovaMCD(8, 12)
        self.assertEqual(prova1.trova_max_com_div(), 4)
        prova2 = my_math.TrovaMCD(5, 9)
        self.assertEqual(prova2.trova_max_com_div(), 1)

    def test_pitagora(self):
        prova1 = my_math.Pitagora(3, 4)
        self.assertEqual(prova1.ipotenusa(), 5)

    def test_coeff_bin(self):
        prova1 = my_math.CoBin(7, 4)
        self.assertEqual(prova1.coeff_bin(), 35)

if __name__ == "__main__":
    unittest.main()
