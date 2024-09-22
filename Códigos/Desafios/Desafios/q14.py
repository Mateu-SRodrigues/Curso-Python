# Q.14) Soma dos dígitos de um número
num = input('Digite um número inteiro: ')
soma = 0

for x in num: # x dentro da lista num []
    valor = int(x) # valor recebe cada caractere da lista num [] como inteiro
    soma += valor # Soma que antes tinha o valor 0 agora soma todas as caracteres e atribui para si

print('A soma dos dígitos desse número é:', soma)