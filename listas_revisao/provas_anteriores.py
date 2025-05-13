#11
#-10
#12.5
#4
#2.5

#1
#print(1 - 2 + 3 * 4)
#print(1 * 2 - 3 * 4)
#print(1 / 2 + 3 * 4)
#print(1 // 2 * 3 + 4)
#print(1 + 2 * 3 / 4)

#2
#n = input("Digite três números separados por espaços:\n")
#nums = n.split()
#soma = 0
#for i in range(3):
#  if int(nums[i]) % 2 == 0:
#    soma = soma + int(nums[i])
#print(f"Soma dos pares: {soma}")

#3

#f = input("Escreva uma frase:\n")
#frase = f[::2]
#print(frase)

#4

#class Agua:
#   def __init__(self):
#    self.mes = 1
#    self.ano = 2025
#    self.consumo = 0
#   def valor(self):
#     if self.consumo <= 10: return 38
#    if self.consumo >= 21: return 38 + 50 + (self.consumo - 20) * 6

#x = Agua()
#x.mes = int(input("Informe o mês da conta: "))
#x.ano = int(input("informe o ano: "))
#x.consumo = int(input("informe o consumo em metros cúbicos "))
#print(f"O valor da conta de água do mês {x.mes} do ano {x.ano} é de {x.valor()} reais.")

#class Circulo:
#    def __init__(self):
#      self.raio = 0
#      self.pi = 3.14
#    def area(self):
#      self.area = self.pi * self.raio**2
#      return self.area
#    def circunferencia(self):
#      self.circunferencia = (2 * self.pi) * self.raio 
#      return self.circunferencia
#x = Circulo()
#x.raio = 5
#print(f"A área do circulo de raio {x.raio} é {x.area()}")
#print(f"A circunferência do circulo de raio {x.raio} é {x.circunferencia()}")

#class Conta:
#    def __init__(self):
#      self.nome = "Nome"
#      self.numero = 1
#      self.saldo = 0
#    def deposito(self):
#      self.deposito = int(input("Quanto deseja depositar? "))
#      self.saldo = self.saldo + self.deposito
#      return self.saldo
#    def saque(self):
#      self.saque = int(input("Quanto deseja retirar? "))
#      self.saldo = self.saldo - self.saque
#      return self.saldo
#x = Conta()
#x.nome = "Sofia"
#print(f"Nome: {x.nome}")
#x.numero = 1234567
#print(f"Numero: {x.numero}")
#x.saldo = 1000
#print(f"Saldo: {x.saldo}")
#print(f"Saldo atual: {x.deposito()}")
#print(f"Saldo atual: {x.saque()}")