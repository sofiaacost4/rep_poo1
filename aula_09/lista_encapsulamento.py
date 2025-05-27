class Conta:
    def __init__(self):
        self.__titular = ""
        self.__numero = ""
        self.__saldo = 0.0
    def set_titular(self,t):
        if t == "": raise ValueError()
        self.__titular = t
    def get_titular(self):
        return self.__titular
    def set_numero(self,n):
        if n == "": raise ValueError()
        self.__numero = n
    def get_numero(self):
        return self.__numero
    def get_saldo(self):
        return self.__saldo
    def depositar(self,v):
        if v < 0: raise ValueError()
        self.__saldo += v
    def sacar(self,v):
        if v<0: raise ValueError()
        if v>self.__saldo:raise ValueError()
        self.__saldo -= v

class UI:
    @staticmethod
    def main():
        x = Conta()
        x.set_titular(input("DIGITE SEU NOME: "))
        x.set_numero(input("DIGITE SEU NUMERO: "))
        x.depositar(float(input("DEPOSITE UM VALOR: ")))
        print(x.get_saldo())

UI.main()