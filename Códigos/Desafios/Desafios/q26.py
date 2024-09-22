# Q.26) Substitur espaços por hífen
texto = input('Insira um texto: ')
sem_esp = ''

for s in texto:
    if s != ' ':
        sem_esp += s
    else:
        sem_esp += '-'

print('Texto sem espaço:', sem_esp)