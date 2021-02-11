def codificar(mensagem: str = 'ola eu sou fabricio'):
    """Codifica uma mensagem e retorna ela codificada"""
    lista = [['a', '!'], ['b', '@'], ['c', '#'], ['d', '$'], ['e', '%'],
             ['f', '&'], ['g', '*'], ['h', '+'], ['i', '^'], ['j', '<'],
             ['k', '>'], ['l', ';'], ['m', '/'], ['n', '°'], ['o', '?'],
             ['p', '|'], ['q', ','], ['r', '('], ['s', ')'], ['t', '{'],
             ['u', '}'], ['w', '['], ['x', ']'], ['y', '~'], ['z', ':'],
             [' ', '_']]

    mensagem = mensagem.lower()

    mensagem_codificada = ''

    for caractere in mensagem:
        for letra in lista:
            if caractere in letra[0]:
                mensagem_codificada += letra[1]

    return mensagem_codificada


def decodificar(mensagem: str = '?;!_%}_)?}_&!@(^#^?'):
    """Decodifica uma mensagem codificada e retorna ela descodificada"""
    lista = [['a', '!'], ['b', '@'], ['c', '#'], ['d', '$'], ['e', '%'],
             ['f', '&'], ['g', '*'], ['h', '+'], ['i', '^'], ['j', '<'],
             ['k', '>'], ['l', ';'], ['m', '/'], ['n', '°'], ['o', '?'],
             ['p', '|'], ['q', ','], ['r', '('], ['s', ')'], ['t', '{'],
             ['u', '}'], ['w', '['], ['x', ']'], ['y', '~'], ['z', ':'],
             [' ', '_']]

    mensagem_decodificada = ''

    for caractere in mensagem:
        for letra in lista:
            if caractere in letra[1]:
                mensagem_decodificada += letra[0]

    return mensagem_decodificada


codificado = codificar('Oi me chamo fabricio')
print(f'A mensagem codificada é {codificado}.')
decodificada = decodificar(codificado)
print(f'A mensagem descodificada fica {decodificada}')
