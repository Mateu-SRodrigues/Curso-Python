texto = input('Digite seu texto: ')


texto = texto.upper()


# processamento
tradutor = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----'
}


chaves_dicionario = tradutor.keys()


texto_morse = ''


for caractere in texto:
    if caractere in chaves_dicionario:
        codigo_morse = tradutor[caractere]


        texto_morse += codigo_morse + ' '


    elif caractere == ' ':
        texto_morse += '/ '


# saída
print('Código Morse:', texto_morse)


frase = texto


#
# Implementado pelo Anderson Costa.
#


import winsound
f = 2500  # Especifica a frequência em 2500 Hertz
t1 = 250  # Especifica o tempo em 1000 ms == 1 segundo
t2 = 125  # Especifica o tempo em 500 ms == 0.5 segundo
for letra in frase:
    if letra == ' ':
        winsound.Beep(37, 125)
    else: 
        morse = tradutor[letra]
        for y in morse:
                if y == '.':
                    winsound.Beep(f, t2)
                if y == '-':
                    winsound.Beep(f, t1)
    winsound.Beep(37, 125)
