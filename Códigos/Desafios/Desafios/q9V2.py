# Q.9) Contar palavras em uma string
texto = input('Digite seu texto: ')
lista = texto.split(' ') 
contador = len(lista)

print('O número de palavras é:', contador)