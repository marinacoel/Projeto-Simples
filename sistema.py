from menu import *
from time import sleep
from arquivo import *
import os

arq = 'nomes.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True: 
    os.system("cls")
    resposta = comando(['Ver pessoas Cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if resposta == 1: 
        #Opção de listar o conteúdo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('NOvO CADASTRO')
        nome = str(input('Digite o nome: '))
        idade = leiaInt('Digite a idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        print('Saindo do sistema... Até logo!')
        break
    else:
        print('Erro. Digite um número válido.')
    input("Pressione ENTER para continuar...")

