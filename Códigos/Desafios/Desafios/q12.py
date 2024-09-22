# Q.12) Maior e menor número de uma Lista

lista = [-2, 45, 2, 98, -100]
maior = lista[0]
menor = lista[0]

for valor in lista:
    if valor > maior:
        maior = valor # 'maior' atualiza 
        
    if valor < maior:
        menor = valor

print('Maior:', maior)
print('Menor:', menor)