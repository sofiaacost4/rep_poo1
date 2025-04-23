def formatar_nome(nome):
   return nome[0].upper() + nome[1:].lower()

n = input("Insira seu nome:")

print(formatar_nome(n))