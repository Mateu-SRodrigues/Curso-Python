# Q.3 Contar vogais em string

texto = input('digite seu texto: ')

contador = 0

for c in texto: # Para todo c pertencente à 'texto':
    if c in ['a', 'e', 'i', 'o', 'u']: # Se o valor de c estiver em a, e , i, o ou u:
        contador += 1

print('Quant. de vogais:', contador)