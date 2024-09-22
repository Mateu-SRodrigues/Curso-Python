# Q.20) Cálculo de média
num = input('Digite os números:', ) # Pesso uma entrada ao usuário
lista = num.split() # Transformo 'num' em uma lista e atribuo como o valor da var 'lista'
soma = 0 # Crio uma var soma com o valor = 0

for x in lista: # Para x pertencente à 'num':
    valor = int(x) # 'valor' é igual a 'x' e 'x' é igual a todos os elementos de 'num', de maneira inteira
    soma += valor # 'soma' recebe 'valor', += (todos os elementos de 'valor' são somados em 'soma')
    media = (soma / (len(lista))) # 'media' = 'soma' divido pelo número de lemento (len) da lista 'num'
print(media)