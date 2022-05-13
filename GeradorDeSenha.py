from tkinter import *
import random

#  Estrutura básica da janela
janela = Tk()
janela.title('Gerador de Senha')
janela.geometry('600x300')
janela.resizable(False, False)
rdioValor = IntVar()

#  Entrada de dados do tamanho
entrada_tamanho = Entry(width=4)
entrada_tamanho.place(x=225, y=50)

# Variáveis com as listas das combinações
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


# Funções das combinações
def letra_num_carac():
    quantidade = int(input('Quantos caracteres terá sua senha? '))
    senha = []
    for c in range(1, quantidade + 1):
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


#  Estrutura dos botões de combinação
estrutura = LabelFrame(janela, text='Escolher combinação')
estrutura.place(x=300, y=50, width=250, height=220)

#  Botões combinação
rdio1 = Radiobutton(estrutura, text='Letra - Número - Caractere especial',
                    variable=rdioValor, value=0, font=('arial', 9),
                    command=letra_num_carac)
rdio2 = Radiobutton(estrutura, text='Letra - Número ', variable=rdioValor, value=1, font=('arial', 9),
                    command=letra_num)
rdio3 = Radiobutton(estrutura, text='Letra - Caractere especial', variable=rdioValor, value=2, font=('arial', 9),
                    command=letra_carac_esp)
rdio4 = Radiobutton(estrutura, text='Número - Caractere especial', variable=rdioValor, value=3, font=('arial', 9),
                    command=num_caracter)
rdio1.grid(row=1, column=0, padx=0, pady=15)
rdio2.grid(row=2, column=0, padx=0, pady=15)
rdio3.grid(row=3, column=0, padx=0, pady=15)
rdio4.grid(row=4, column=0, padx=0, pady=15)

# BotãoCheck excluir repetidos
chkrepetido = Checkbutton(janela, text='Excluir caracter repetido')
chkrepetido.place(x=25, y=100)

#  Texto Escolha de tamanho.
texto_tamanho = Label(janela, text='Escolher o tamanho')
texto_tamanho.place(x=25, y=50)

#  Botão GERAR SENHA
bt_GerarSenha = Button(janela, text='GERAR SENHA', bd='1')
bt_GerarSenha.place(x=100, y=150)

#  Botão COPIAR SENHA
bt_CopiarSenha = Button(janela, text='COPIAR SENHA', bd='1')
bt_CopiarSenha.place(x=100, y=240)

janela.mainloop()
