# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

alunos = {}

alunos['nome'] = str(input('Nome: '))
alunos['media'] = float(input(f'Média de {alunos["nome"]}: '))
if alunos['media'] < 7:
    alunos['situacao'] = 'Reprovado'
else:
    alunos['situacao'] = 'Aprovado'
print(f'Nome do aluno: {alunos["nome"]}\nMédia: {alunos["media"]}\nSituação do aluno: {alunos["situacao"]}')

# Resolução do professor

aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif aluno ['media'] < 7:
    aluno['situacao'] = 'Recuperacao'
elif aluno['media'] < 5:
    aluno['situacao'] = 'Reprovado'
    
for k, v in aluno.items():
    print(f'  - {k} é igual a {v}')

