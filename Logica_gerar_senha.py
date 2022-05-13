import random

todos = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
         'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b',
         'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
         'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
         '!', '#', '$', '%', '"', '&', '*', '( )', '+', '<', '>', ':', '?', '|']
letraEnum = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
             'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b',
             'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
             'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3',
             '4', '5', '6', '7', '8', '9']
letra_caracter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                  'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b',
                  'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                  'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '!', '#', '$', '%',
                  '"', '&', '*', '( )', '+', '<', '>', ':', '?', '|']
numEcaracter = ['!', '#', '$', '%', '"', '&', '*', '( )', '+', '<', '>', ':', '?', '|',
                '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def letra_num_carac():
    quantidade_todos = int(input('Quantos caracteres terá sua senha? '))
    senha = []
    for c in range(1, quantidade_todos + 1):
        escolha = random.choice(todos)
        senha.append(escolha)
    str_senha = "".join(senha)
    print(str_senha)


def letra_num():
    quantidade = int(input('Quantos caracteres terá sua senha? '))
    senha = []
    for c in range(1, quantidade + 1):
        escolha = random.choice(letraEnum)
        senha.append(escolha)
    str_senha = "".join(senha)
    print(str_senha)


def letra_carac_esp():
    quantidade = int(input('Quantos caracteres terá sua senha? '))
    senha = []
    for c in range(1, quantidade + 1):
        escolha = random.choice(letra_caracter)
        senha.append(escolha)
    str_senha = "".join(senha)
    print(str_senha)


def num_caracter():
    quantidade = int(input('Quantos caracteres terá sua senha? '))
    senha = []
    for c in range(1, quantidade + 1):
        escolha = random.choice(numEcaracter)
        senha.append(escolha)
    str_senha = "".join(senha)
    print(str_senha)


letra_num_carac()
letra_num()
letra_carac_esp()
num_caracter()
