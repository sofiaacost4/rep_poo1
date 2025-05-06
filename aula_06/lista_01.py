class Viagem:
    def __init__(self):
        self.distancia = 60
        self.tempo = 60
    def velocidade(self):
        velocidade = self.distancia / self.tempo
        return velocidade


x = Viagem()
x.distancia = 240
x.tempo = 4
print(x.velocidade())
        


