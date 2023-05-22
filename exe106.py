# Faça um mini-sistema que utilize o interactive Help do Python. O usuário vai digitar o comando e o manual
# vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará.

# OBS: use cores.

from time import sleep

c = ('\033[m',        # 0 - Sem cores  
     '\033[0;30;41m', # 1 - Vermelho
     '\033[0;30;42m', # 2 - Verde
     '\033[0;30;43m', # 3 - Amarelo
     '\033[0;30;44m', # 4 - Azul
     '\033[0;30;45m', # 5 - Roxo
     '\033[7m')       # 6 - Branco
     
def titulo(msg, cor = 0):
    tam = len(msg)
    print(c[cor], end='') 
    print('=' * tam)
    print(msg)
    print('=' * tam)
    print(c[0], end='')

def ihelp(pkg):
    titulo(f'Acessando o manual do comando \'{pkg}\'', 4)
    print(c[6], end='')
    help(pkg)
    print(c[0], end='')
    sleep(2)
    
comando = ''
while True:
    titulo('SISTEMA INTERACTIVE HELP DO PYTHON', 2)
    func = str(input("Digite um pacote/função: "))
    if comando.upper() == 'FIM':
        break
    else:
        ihelp(func)
titulo('OBRIGADO PELA PREFERÊNCIA!', 1)