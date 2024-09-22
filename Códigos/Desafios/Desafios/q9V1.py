# Q.9) Contar palavras em uma string
texto = input('Digite seu texto:')

contador = 0 

for c in texto:
    if c == ' ':
        contador += 1

contador += 1
print('O número de palavras é:',contador)