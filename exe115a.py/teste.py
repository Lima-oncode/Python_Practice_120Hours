# Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.

# Exercício Python 115a: O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.

# Exercício Python 115b: Vamos ver como fazer acesso a arquivos usando o Python.

 
# Módulos pessoais
from interface import menu

# Pacotes built-in ou instalados
from time import sleep
from colorama import Style, Fore

while True:
    resposta = menu()
    if resposta == 1:
        print(Style.DIM + Fore.GREEN + 'Ver pessoas cadastradas')
    elif resposta == 2:
        print(Style.DIM + Fore.GREEN + 'Cadastrar nova pessoa')
    elif resposta == 3:
        print(Style.DIM + Fore.GREEN + 'Saindo do sistema... Até logo!')
        break
    else:
        print(Style.BRIGHT + Fore.LIGHTRED_EX + 'ERRO! Digite uma opção válida')
    sleep(5)
print('Volte sempre')
        
# Resolução do professor

from interface_prof import cabecalho, menu

cabecalho('Cadastro v 1.0')

while True:
    resposta = (menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema']))
    if resposta == 1:
        cabecalho('Ver pessoas cadastradas')
    elif resposta == 2:
        cabecalho('Cadastrar nova pessoa')
    elif resposta == 3:
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        print(f'\033[0;31mErro digite uma opção válida!\033[m')    
    sleep(2)