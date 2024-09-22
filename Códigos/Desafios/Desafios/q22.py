# Q.22 Calcular Potência

base = int(input('Digite a base:')) # 3
expoente = int(input('Digite o expoente: ')) # 5

resultado = base

for x in range(expoente - 1):
    resultado = resultado * base

print('Resultado:', resultado)