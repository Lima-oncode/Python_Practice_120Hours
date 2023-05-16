# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as 
# notas de cada aluno individualmente.

dados = []

while True:
    nome = str(input('Digite seu nome: '))
    nota1 = float(input('Digite sua primeira nota: '))
    nota2 = float(input('Digite sua segunda nota: '))
    media = (nota1 + nota2) / 2
    dados.append([nome, [nota1, nota2], media])
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar in 'Nn':
        break
print('-=' * 30)
print(f'{"Nº":<4}{"NOME":<10}{"MEDIA":>8}')
print('-' * 30) 
for i, a in enumerate(dados):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('Finalizando...')
        break
    if opc <= len(dados) - 1:
        print(f'Notas de {dados[opc][0]} são {dados[opc][1]}')

# Resolução do professor

ficha = []

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
# Este print serve para gerar o cabeçalho acima dos dados o comando ':> ou :<' serve pra indicar onde
# o mesmo vai ser posicionado
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print('-' * 30)
# em enumerate a primeira variável é o indice (i) e (a) se refere a valores na lista
# onde (a[0]) se refere ao nome do aluno e a[2] se refere a média do aluno  
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('Finalizando...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')


    
