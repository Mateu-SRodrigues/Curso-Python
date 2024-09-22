# Q.16) Contar ocorrências de caracteres em uma string
txt = input('Digite um texto: ')
caractere = input('Qual caractere você quer saber a ocorrência: ')

cont = 0

for c in txt:
    if c in caractere:
        cont += 1
print(cont)
