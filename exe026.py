''' 
Faça um programa que leia uma frase e retorne:
1 - Quantas vezes aparece a letra 'a'
2 - Em que posição ela aparece a primeira vez
3 - Em que posição ela aparece a última vez 

'''

frase = str(input('Digite qualquer frase: ').strip().lower())

count_a = print(frase.count('a'))
pos_primeira_vez = print(frase.find('a')+1)
pos_ultima_vez = print(frase.rfind('a')+1)

# Resolução do professor

frase = str(input('Digite uma frase: ').upper().strip())

print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A ultima letra A apareceu na posição {}'.format(frase.rfind('A')+1))


