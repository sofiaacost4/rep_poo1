class Circulo:
    def __init__(self):
        self.__r = 0
        self.__pi = 3.14
    def calc_area(self):
        return self.__r * (self.__pi**2)
    def calc_circunferencia(self):
        return (2*self.__r) * self.__pi
    def get_raio(self):
        return self.__r



class UI:
    @staticmethod
    def main():

