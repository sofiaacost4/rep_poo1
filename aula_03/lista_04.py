#1151

f = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

n = int(input())
s = []
for i in range(n):
    s.append(f[i])

print(str(s).replace(",","").replace("[","").replace("]",""))






