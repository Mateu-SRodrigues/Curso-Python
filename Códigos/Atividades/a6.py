# A.6) Sistema de gerenciamento de regisros de funcionários
lista_func = []
novo_id = 1
# 1. função: ADICIONAR FUNCIONÁRIO
def add_func():
    global novo_id
    novo_func = {}

    novo_func['nome'] = input('Informe o nome de funcionário: ')
    novo_func['id'] = novo_id
    novo_func['cargo'] = input('Informe o cargo do funcionário: ')
    novo_func['salario'] = input('Informe o salário do funcionário: ')

    lista_func.append(novo_func)
    novo_id += 1
# 2. função: BUSCAR USUÁRIO PELO ID
def buscar_func():
    id = int(input('Digite o ID do funcionário: '))

    func_encontrado = 0

    for func in lista_func:
        if func['id'] == id:
            func_encontrado = func

    if func_encontrado == 0:
        print('Funcionário não existe!')
    else:
        print('Nome:', func_encontrado['nome'], end = ', ')
        print('ID:', func_encontrado['id'], end = ', ')
        print('Cargo:', func_encontrado['cargo'], end = ', ')
        print('Salário:', func_encontrado['salario'])
# 3. função: EDITAR FUNCIONÁRIO
def editar_func():
    print('Editar dados do funcionário:\n 1. Editar nome\n 2. Editar Cargo\n 3. Editar salário\n 4. Todas as opções')
    opcao = int(input('Escolha uma opção: '))
    id = int(input('Informe o ID para edição: '))

    for func in lista_func:
        if func['id'] == id:
            
            if opcao == 1:
                novo_nome = input('Edite o nome do funcionário: ')
                func['nome'] = novo_nome
            elif opcao == 2:
                novo_cargo = input('Edite o cargo: ')
                func['cargo'] = novo_cargo
            elif opcao == 3:
                novo_salario = input('Edite o salário: ')
                func['salario'] = novo_salario
            elif opcao == 4:
                novo_nome = input('Edite o nome do funcionário: ')
                func['nome'] = novo_nome

                novo_cargo = input('Edite o cargo: ')
                func['cargo'] = novo_cargo

                novo_salario = input('Edite o salário: ')
                func['salario'] = novo_salario
                print('Nome editado:', novo_nome, end = '\n')
                print('Cargo editado:', novo_cargo, end = '\n')
                print('Salário editado:', novo_salario, end = '.')
                break
        else:
            print('\nInsira um ID válido!\n')
# 4. função: DELETAR FUNCIONÁRIO
def delet_func():
    id = int(input('Digite o ID do funcionário que deseja deletar: '))
    func_encontrado = 0

    for func in lista_func:
        if func['id'] == id:
            func_encontrado = func
            break

    if func_encontrado == 0:
        print('Funcionário não existe!')
    else:
        lista_func.remove(func_encontrado)
        print('\nFuncionário deletado!\n')

# 5. função: LISTAR TODOS OS FUNCIONÁRIOS
def listar_func():
    print('Lista de Funcionários:')

    for func in lista_func:
        print('Nome:', func['nome'], end = ',')
        print('ID:', func['id'], end = ',')
        print('Cargo:', func['cargo'], end = ',')
        print('Salário:', func['salario'])

# menu
opcao = 0

while opcao != 6:
    print('\nGESTÃO DE FUNCIONÁRIOS\n')
    print('1. Adicionar funcionário')
    print('2. Buscar funcionário')
    print('3. Editar funcionário')
    print('4. Deletar funcionário')
    print('5. Listar todos os funcionários')
    print('6. Sair\n')

    opcao = int(input('Escoha uma opção: '))

    if opcao == 1:
        add_func()
    elif opcao == 2:
        buscar_func()
    elif opcao == 3:
        editar_func()
    elif opcao == 4:
        delet_func()
    elif opcao == 5:
        listar_func()
    elif opcao == 6:
        print('\nPROGRAMA FINALIZADO.\n')