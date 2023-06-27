class Bola:
    def __init__(self):
        self.cor = 'Amarelo'
        self.circonferencia = True
        self.material = 'Plastico'

    def trocaCor(self):
        self.cor = 'Roxo'

    def mostraCor(self):
        self.trocaCor()


b1 = Bola()
print(b1.cor)
print(b1.circonferencia)
print(b1.material)

b2 = Bola()
b2.mostraCor()
print(b2.cor)
