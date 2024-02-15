from math import sqrt

class MathException(Exception):
    pass


class TrovaDivisori():
    def __init__(self, num):
        if num <= 0:
            raise MathException("Il numero deve essere positivo")
        self.num = num

    def trova_divisori(self):
        divisori = []
        for i in range (1, self.num + 1):
            if self.num % i == 0:
                divisori.append(i)
        return divisori


class TrovaDivisoriComuni(TrovaDivisori):
    def __init__(self, num1, num2):
        super().__init__(num1)
        self.num2 = num2

    def trova_divisori(self):
        divisori2 = super().trova_divisori()
        return divisori2
    
    def trova_divisori_comuni(self):
        divisori1 = self.trova_divisori()
        divisori2 = TrovaDivisori(self.num2).trova_divisori()
        divisori_comuni = []

        for element in divisori1:
            if element in divisori2:
                divisori_comuni.append(element)
        if not divisori_comuni:
            print("Non esistono divisori comuni")
        else:
            return divisori_comuni


class TrovaMCD(TrovaDivisoriComuni):
    def trova_max_com_div(self):
        lista_div = self.trova_divisori_comuni()
        if lista_div is not None:
            return max(lista_div)


class Pitagora():
    def __init__(self, cat1, cat2):
        if cat1 <= 0 or cat2 <= 0:
            raise MathException("I cateti devono avere valore positivo")
        self.cat1 = cat1
        self.cat2 = cat2

    def ipotenusa(self):
        return(sqrt(self.cat1 ** 2 + self.cat2 ** 2))


class CoBin():
    def __init__ (self, n, k):
        if n < k:
            raise MathException("k deve essere minore di n")
        if n <= 0 or k <= 0:
            raise MathException("n e k devono essere due numeri positivi")
        self.n = n
        self.k = k

    def coeff_bin(self):
        prod = 1
        for i in range (self.n - self.k +1, self.n + 1):
            prod *= i
        k_fatt = 1
        for i in range (1, self.k + 1):
            k_fatt *= i
        ris = prod / k_fatt
        return ris


class MediaPonderata():
    def __init__ (self, voti, pesi):
        if not voti or not pesi:
            raise MathException("Errore, lista vuota")
        if len(voti) != len(pesi):
            raise MathException("Errore, numero voti diverso da numero pesi")
            
        self.pesi = sum(pesi)
        self.voti = []
        for i in range(len(voti)):
            voto = voti[i] * pesi[i]
            self.voti.append(voto)

    def media_pond(self):
        somma = sum(self.voti)
        return somma / self.pesi
        