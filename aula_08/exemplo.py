class Triangulo:
    def __init__(self):
        self.b = 0
        self.h = 0
    def set_b(self,v):
        if v < 0: raise ValueError("A base deve ser positiva")
    def set_h(self,v):
        if v < 0: raise ValueError("A altura deve ser positiva")
    def calc_area(self):
        return self.b * self.h / 2
    
class UI:
    @staticmethod
    def menu():
        op = int(input("Escolha uma opção: 1 - Triangulo | 2 - Fim \n" ))
        return op
    @staticmethod
    def main():
        op = 0
        while op != 2:
            op = UI.menu()
            if op == 1: UI.triangulo()
    @staticmethod
    def triangulo():
        x = Triangulo()
        x.b = int(input("Informe o valor da base:"))
        x.h = int(input("Informe o valor da altura:"))
        if x.h < 0: raise ValueError("A altura deve ser positiva")
        print(f"O triângulo de base {x.b} e altura {x.h} tem área {x.calc_area()}")

UI.main()