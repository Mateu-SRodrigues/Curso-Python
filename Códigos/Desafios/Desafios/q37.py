# Q.37 Contar palavras com um determinado comprimento.

texto = input('Digite seu texto: ')
comprimento = int(input('Digite o comprimento para contar: '))

lista_palavras = texto.split()

contador = 0

for palavra in lista_palavras:
    if len(palavra) == comprimento:
        contador += 1

print('Quantidade de palavras:', contador)
