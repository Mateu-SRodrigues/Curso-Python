# Q.19) Remover vogais de uma string
texto = input('Digite o texto: ')
v = ['a', 'e', 'i', 'o', 'u']
sem_vogais = ''

for c in texto:
    if c not in v: # SE c não estiver contido em vogais irá sobrar somente as consoantes
        sem_vogais += c # sem_vogais recebe somente as consoantes

print('O texto sem vogais é:', sem_vogais)
