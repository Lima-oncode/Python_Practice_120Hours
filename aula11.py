'''
ANSI escape sequence :

O código ANSI começa com contra barra '\' e depois vem o código
o código que funciona melhor para python com cores é o '(033)
sempre que quiser representar uma cor em python: \033[m]
entre o inicio do colchete e o 'm' são colocados até 3 códigos que representam as caracteristicas
\033[(1° valor = style), (2° valor = text), (3° valor = back)m
\033[0:33:44m
'''

'''
Para facilitar, segue a tabela de seqüência de escape ANSI:

(código 1° valor - STYLE - Iniciando do 0 e indo até o 7)

none = '\033[0m'
bold/negrito = '\033[1m'
underline/sublinhado = '\033[4m'
negative/inverte = '\033[7m'


(código 2° valor - TEXT - Iniciando do 30 e indo até o 37)

preto = '\033[30m'
vermelho = '\033[31m'
verde = '\033[32m'
amarelo = '\033[33m'
azul = '\033[34m'
magenta = '\033[35m'
ciano = '\033[36m'
branco = '\033[37m'

(código 3° valor - BACK - Iniciando do 40 e indo até o 47)

fundo preto = '\033[40m'
fundo vermelho = '\033[41m'
fundo verde = '\033[42m'
fundo amarelo = '\033[43m'
fundo azul = '\033[44m'
fundo magenta = '\033[45m'
fundo ciano = '\033[46m'
fundo branco = '\033[47m'
'''
#\033[0:30:41m
#\033[4:33:44m
#\033[1:35:43m
#\033[30:42m
#\033[m
#\033[7:30m

# -- Colocando em prática
# Estudar módulo colorize

print('\033[4;35;45m Olá mundo\033[m')
print('\033[7;33;44m Olá mundo\033[m')

a = 3
b = 5

print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a, b))

nome = 'Lucas'

cores = {'limpa': '\033[m', 
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretobranco':'\033[7;37m'}

print('Olá, prazer em te conhecer {}{}{}'.format(cores['pretobranco'], nome, cores['limpa']))

