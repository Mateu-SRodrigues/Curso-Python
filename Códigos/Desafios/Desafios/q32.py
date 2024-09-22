# Imprimir múltiplos de N

num = int(input('Digite o número: '))
limite = int(input('Informe um limite: '))

for m in range(num, num * limite + 1, num):
    print(m)