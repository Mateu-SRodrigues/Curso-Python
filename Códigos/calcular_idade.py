import datetime

def calcularIdade():
    anoatual = int(input('Em que ano você nasceu?'))
    x = datetime.date.today().year
    y = x - anoatual

    idade = int(input('Qual a sua idade?'))

    if idade == y:
        print('Tudo certo!')
    else:
        print('A idade informada não conrresponde com à caculada com base no ano de nascimento!')
        return(calcularIdade())
print(calcularIdade())