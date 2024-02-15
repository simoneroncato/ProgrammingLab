class ExamException(Exception):
    pass

class MovingAverage():
    def __init__(self, l_finestra):
        if l_finestra <= 0 or not isinstance(l_finestra, int):
            raise ExamException("Errore, finestra non è numero intero positivo")
        self.l_finestra = l_finestra

    def compute(self, lista):
        if not lista:
            raise ExamException("Errore, lista valori vuota")
        
        if len(lista) < self.l_finestra:
            raise ExamException("Errore, lunghezza finestra maggiore di lunghezza lista")

        medie = []
        for i in range(len(lista) - self.l_finestra +1):
            finestra = lista[i : i + self.l_finestra]
            media = sum(finestra) / self.l_finestra
            medie.append(media)

        return(medie)


