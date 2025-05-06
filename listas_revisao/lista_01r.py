#4

print("Digite o primeiro horário no formato hh:mm")
h_1 = input()
print("Digite o segundo horário no formato hh:mm")
h_2 = input()

hora1 = list(h_1)
hora2 = list(h_2)

i = 0
soma = 0
for i in range(5):
    if i != 2:
        if i == 3 and soma > 6:
            soma = int(hora1[1]) + int(hora2[1]) + 1
        else:
            soma = int(hora1[i]) + int(hora2[i])
        print(soma)

    
print(f"Total de horas:{soma}")