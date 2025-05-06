class Viagem:
    def __init__(self):
        print("Insira a distância da viagem em metros:")
        self.distancia = int(input())
        print("Insira o tempo total da viagem em minutos:")
        self.tempo = int(input())
    def velocidade(self):
        velocidade = self.distancia / self.tempo
        return velocidade


x = Viagem()
print(x.velocidade())
        


