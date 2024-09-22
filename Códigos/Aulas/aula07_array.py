# Índice:          0        1         2
lista_nomes = ['Mateus', 'Varlen', 'Savio']

print(lista_nomes) # Printa o array, inclusive colchetes e vírgulas
print(lista_nomes[0]) # Printa somente o nome de acordo com o índice

lista_nomes[0] = 'Anderson' # Troca o índice 0 ('Mateus') por 'Anderson'

print(lista_nomes)
print(lista_nomes[0])

for indice in range(3): 
    print('Índice:', indice)
    print(lista_nomes[indice]) # Printa os três índices, do 0 ao 2

lista_nomes = [
    'Anderson', 
    'Varlen',
    'Mateus',
    'Saviu',
    'Larissa',
    'Lucas'
]
print(lista_nomes)

print(len(lista_nomes)) # 'len' me diz quantos elementos eu tenho no array

lista_nomes.append('Lucas') # Adiciona mais um 'Lucas' há lista
print(lista_nomes)

indice = lista_nomes.index('Anderson') # Verifica a posição de um valor expecífico
print(indice)

lista_nomes.remove('Lucas') # Remove um valor 'Lucas' da lista
print(lista_nomes)

lista_nomes.sort(reverse=True) # 'sort' organiza a lista em ordem alfabética, ou o contrário, ordem crescente e decrescente
print(lista_nomes)