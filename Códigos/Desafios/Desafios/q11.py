# Q.11) Converter temperatura

print('Selecione a alternativa: \n a)°C->°F \n b)°F->°C') # Pedindo uma entrada
alt = input('Informe a alternativa para a converção: ') # Valor da entrada

temp = float(input('Informe a temperatura: ')) # Pedindo uma segunda entrada

if alt == 'a' or alt == 'A': # Processamento
    a = (temp * 1.8 + 32)
    print('O resultado da converção é de:', a,' °F.') # Saída
elif alt == 'b' or alt == 'B': # Processamento
    b = ((temp - 32)/1.8)
    print('O resultado da converção é de:', b,' °C.') # Saída
else:
    print('Operação encerrada, corrija a alternativa ou a temperatura!') # Saída