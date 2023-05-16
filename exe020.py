#O professor agora quer sortear uma ordem de apresentação entre os alunos, mostre a ordem.
from random import shuffle
al1 = input('1º aluno')
al2 = input('2º aluno')
al3 = input('3º aluno')
al4 = input('4º aluno')
grp = [al1,al2,al3,al4]
seq = shuffle(grp)
print('A sequência sorteada foi')
print(grp)