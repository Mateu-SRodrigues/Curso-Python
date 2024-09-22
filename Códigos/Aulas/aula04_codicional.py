
entrada = input('Qual sua idade? ')

idade = int(entrada)

# >= <= > < == !=

if idade >= 18: # Se idade maior ou igual a 18:
    print('Maior de idade!')
else:   # Se não:
    print('Menor de idade!')
if idade > 65: # Se idade maior ou igual a 65:
    print('Aposentado.')
else:    # Se não:
    print('Não é aposentado, hora de se aposentar.')