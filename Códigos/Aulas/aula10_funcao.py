
def somar(a, b): # Definindo o nome da função commo 'somar' e passando seus parâmetros (a, b), os números que serão somados
    resultado = a + b # Var 'resultado' recebe como valor a soma de a + b

    return resultado # Retorno da var soma

def fatorial(numero):
    resultado = numero

    for valor in range(numero - 1, 0, -1):
        resultado = resultado * valor
        
    return resultado

resultado = somar(3, 6)
print(resultado)

resultado = fatorial(5)
print(resultado)
