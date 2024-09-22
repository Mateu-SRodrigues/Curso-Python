# Q.15) Remover duplicatas de uma lista
lista = [2,2,-5,40,40,24]
sem_duplicatas = []

for valor in lista:
    if valor not in sem_duplicatas:
        sem_duplicatas.append(valor)
print(sem_duplicatas)