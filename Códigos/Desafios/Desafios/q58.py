# Q.58) Tradutor para código morse
texto = input('Digite seu texto: ')
texto = texto.upper()

tradutor = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----'
}

chaves_dicionario = tradutor.keys()
texto_morse = ''

for caractere in texto:
    if caractere in chaves_dicionario:
        codigo_morse = tradutor[caractere]
        texto_morse += codigo_morse + ' '

    elif caractere == ' ':
        texto_morse += '/'

print(texto_morse)