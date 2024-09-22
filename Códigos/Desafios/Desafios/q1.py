# CALCULADORA DE IMC

peso = float(input('Digite seu peso, em KG:\n> ')) # Tipo float
altura = float(input('Dgite sua altura, em M:\n> ')) # Tipo float

imc = float(peso / (altura**2))
print ('Seu ídice de massa compórea é: ', imc)

if imc < 18.5:
    print('Magreza')
if imc >= 18.5 and imc < 25:
    print('Adequado')
if imc >=25  and imc < 30:
    print('Pré-obeso')
if imc >= 30:
    print('Obeso')