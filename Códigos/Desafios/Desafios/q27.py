# Q.27) Converter minutos em horas e minutos
minutos = input('Informe os minutos: ')

for c in minutos:
    c = int(minutos)
    hora = int((c / 60))
    min = int((c % 60))
print('A conversão é:', hora, 'horas e', min, 'minutos')