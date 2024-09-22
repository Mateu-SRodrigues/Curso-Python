# Q.4 Verificar palíndromo

texto = input('Digite uma frase ou palavra: ')

novo_texto = texto.replace(' ', '') # A função replace() retorna o valor da var texto substituindo os ' ' por '' (Retirou os espaços)
novo_texto = novo_texto.lower() # A função lower() converte toda a string da var nomvo_texto em minúsculo

if novo_texto == novo_texto[::-1]: # Se novo_texto for igual a novo_texto de trás para fente:
    print('É palíndromo.')
else:
    print('NÃO é palíndromo.')