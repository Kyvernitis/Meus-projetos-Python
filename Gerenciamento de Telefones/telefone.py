def add_reg():
    """Adiciona um novo registro de telefone."""
    name = str(input('Nome: '))
    while len(name) > 20:
        print('Nome invalido, maior que 20 caracteres.', end=' ')
        name = str(input('Nome: '))

    phone_number_dd = int(input('DD do numero: '))
    phone_number_tel = str(input('Numero sem o DD e traço: '))
    phone_number = f'{phone_number_dd} {phone_number_tel} \n'
    phone_reg = [f'{name:20}', phone_number]
    print(phone_reg)
    reg = open('reg.txt', 'a+')
    reg.writelines(phone_reg)
    reg.close()
    menu()


def show_reg():
    """Exibe os registros telefonicos cadastrados."""
    reg = open('reg.txt', 'r+')
    regs = reg.readlines()
    for pos, line in enumerate(regs):
        print(f'{pos + 1} - {line}', end='')
    reg.close()


def change_reg():
    """Muda algum registro."""
    print('---' * 10)
    show_reg()
    op = int(input('Qual registro você quer mudar: '))
    with open('reg.txt', 'r+') as arq_reg:
        regs = arq_reg.readlines()
        while op > len(regs):
            print('REGISTRO NÃO EXISTENTE.')
            show_reg()
            op = int(input('Qual registro você quer mudar: '))
        print('Registro encontrado!')
        op_name = int(
            input('''Você quer mudar o nome[1], numero[2] ou cancelar[3]? '''))
        while op_name not in [1, 2, 3]:
            print('Resposta invalida! Tente novamente.')
            op_name = int(
                input('''Mudar o nome[1], numero[2] ou cancelar[3]? '''))
        if op_name == 1:
            new_name = str(input('Novo nome: '))
            while len(new_name) > 20:
                print('Nome invalido, maior que 20 caracteres.')
                new_name = str(input('Nome: '))
            new_reg = [f'{new_name:20}', regs[op - 1][20:]]
            regs[op - 1] = new_reg
            print(regs)
        elif op_name == 2:
            new_dd_number = int(input('DDD do novo numero: '))
            new_number = int(input('Numero: '))
            new_phone_number = f'{new_dd_number} {new_number}\n'
            new_reg = [f'{regs[op - 1][:20]}{new_phone_number}']
            regs[op - 1] = new_reg
        elif op_name == 3:
            menu()
            return 0
    arq_reg.close()

    arq1 = open('reg.txt', 'w+')
    for reg in regs:
        print(reg)
        arq1.writelines(reg)
    arq1.close()
    menu()


def search_reg():
    """Procura um registro através do nome;"""
    print('---' * 10)
    name = str(input('Nome: '))
    regs_search = []
    with open('reg.txt') as arq_reg:
        reg = arq_reg.readlines()
        for phone_number in reg:
            if name.upper() in phone_number.upper():
                regs_search.append(phone_number)
    if len(regs_search) != 0:
        print('Numeros achados: ')
        for number in regs_search:
            print(number, end='')
    else:
        print('Registro de telefone não encontrado.')
        menu()


def remove_reg():
    """Remove um registro telefonico."""
    print('---' * 10)
    show_reg()
    op = int(input('Qual registro você quer remover: '))
    with open('reg.txt', 'r+') as arq_reg:
        regs = arq_reg.readlines()
        while op > len(regs):
            print('REGISTRO NÃO EXISTENTE.')
            show_reg()
            op = int(input('Qual registro você quer remover: '))
        print('Registro encontrado e Deletado!')
        del regs[op - 1]
    arq_reg.close()
    with open('reg.txt', 'w+') as arq_reg:
        for reg in regs:
            arq_reg.write(reg)
    menu()


def menu():
    """Mostra o menu de ações."""
    print('''Sistema de Gerenciamento de Telefones

(1) Adicionar registro telefonico.
(2) Mostrar registros telefonicos.
(3) Pesquisar registros telefonicos.
(4) Modificar registro telefonico.
(5) Apagar registro telefonico.
(6) Sair do Sistema.
''')
    op = int(input('Sua escolha: '))
    if op == 1:
        add_reg()
    elif op == 2:
        show_reg()
        menu()
    elif op == 3:
        search_reg()
    elif op == 4:
        change_reg()
    elif op == 5:
        remove_reg()
    elif op == 6:
        print('Saindo...')
        return 0
    else:
        return 0
