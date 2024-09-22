
# A chave do dictionary é sempre uma espécie de string
pessoa = {
    #chave
    'nome': 'Mateus Silva', 
    'idade': 29,
    'cpf': '123.456.789-01',
    'altura': 1.76,
    'veículo': {
        'marca': 'ford',
        'modelo': 'civic',
        'ano': 2005
    }
}

print(pessoa)
print(pessoa['veículo']['marca'])

pessoa['nome'] = 'Mateus' # Altero o valor da chave 'nome' para 'Mateus' 
print(pessoa)

pessoa['peso'] = 76
print(pessoa)

lista_pessoas = [
    {
        'nome': 'Paulo',
        'idade': 18
    },
    {
        'nome': 'Davi',
        'idade': 32
    },
    {
        'nome': 'Larissa',
        'idade': 16
    }
]

print(lista_pessoas[0]['nome']) # lista_pessoas [0] representa o índice principal, 'lista_pessoas' é um array