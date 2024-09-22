# Q.10) Sequência de Fibonacci
n_termos = int(input('Digite quantos termos: '))

penultimo = 0
ultimo = 1

print(penultimo, ultimo, end = ' ')

for x in range(n_termos - 2):
    proximo = penultimo + ultimo
    print(proximo, end = ' ')

    penultimo = ultimo
    ultimo = proximo
