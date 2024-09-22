
print('MENU CALCULADORA \n A)Somar \n B)Subtrair \n C)Multiplicar \n D)Dividir')
letras = ['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D']

alt = input('Digite a alternativa: ')

if alt in letras:
    print('A alternativa é:', alt)
else:
    print('Alternativa inválida!')
