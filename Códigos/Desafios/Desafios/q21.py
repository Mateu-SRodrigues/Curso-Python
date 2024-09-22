# Q.21) Contar números positivos e negativos
lista = [12, -4, -8, 26, 64, -32, -69, 8, 35, 42]

pos = 0
neg = 0

for v in lista:
    if v > 0:
        pos += 1
    else:
        neg +=1
print('O número de positivos é:', pos)
print('O número de negativos é:', neg)