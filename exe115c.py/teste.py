# Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.

# Exercício Python 115a: O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.
# Exercício Python 115b: Vamos ver como fazer acesso a arquivos usando o Python.
# Exercício Python 115c: Criando a função 'cadastrar' e otimizando a leitura do arquivo.
 
# Módulos pessoais
from interface import menu, filexists, criar_arquivo, ler_arquivo, cabecalho, leiaint, cadastrar

# Pacotes built-in ou instalados
from time import sleep
from colorama import Style, Fore

filename = "115b_cadastro.txt"
if not filexists(filename):
    criar_arquivo(filename)  
   
while True:
    resposta = menu()
    if resposta == 1:
        ler_arquivo(filename)
    elif resposta == 2:
        cabecalho('Cadastrar nova pessoa')
        nome = str(input('Nome: '))
        idade = leiaint('Idade:')
        cadastrar(filename, idade, nome)
    elif resposta == 3:
        print(Style.DIM + Fore.GREEN + 'Saindo do sistema... Até logo!')
        break
    else:
        print(Style.BRIGHT + Fore.LIGHTRED_EX + 'ERRO! Digite uma opção válida')
    sleep(1)
print('Volte sempre')