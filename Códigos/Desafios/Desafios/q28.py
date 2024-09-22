# Q.28 Calcular área e perímetro do retângulo.

def area(a, l): # função: calcular área de retângulo
    return a * l

def perimetro(a, l): # função: calcular o perímetro de retângulo
    return 2 * (a + l)

altura = float(input('Digite a altura do retângulo: '))
largura = float(input('Digite a largura do retângulo: '))

resul_area = area(altura, largura) # Resultado da área = a função area com os parâmetros (altura, largura)
resul_perimetro = perimetro(altura, largura) # Resultado do perímetro = a função perimetro com os parâmetros (altura, largura)

print('Área do retângulo:', resul_area)
print('Perímetro do retângulo:', resul_perimetro)