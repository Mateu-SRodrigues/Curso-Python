# Q.6) Calcular fatorial
print('---> Calcular fatorial <---')
n = int(input('Digite um número: '))
resultdo = 1

for f in range(n, 0, -1): # Para todo 'f' entre o valor de 'n' e 0, NA ORDEM DE -1:
    print(f, end ='') # Print o valor de 'f' seguido de um ' ' ...
    if f != 1: # ..., se 'f' for diferente de 1:
        print(' x ', end='') # Print ' x ' seguido de um ' '
    resultdo *= f # Var 'resultado' recebe os valores de f, dentro da range, multiplicados entre si

print(' =', resultdo)
