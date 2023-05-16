# Crie um programa que leia dois valores e mostre um menu na tela:
# [1] SOMA
# [2] MULTIPLICAR
# [3] MAIOR
# [4] NOVOS NÚMEROS
# [5] SAIR DO PROGRAMA
# Seu programa deverá realizar a operação solicitada em cada caso.

v1 = int(input('Digite o primeiro valor: '))
v2 = int(input('Digite o segundo valor: '))
op = 0


while op != 5:
    op = int(input(
'''
=== Qual operação deseja realizar ===

[1] SOMA
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA
'''
))
    if op == 1:
        print('A soma entre {} e {} é {}'.format(v1, v2, v1+v2))
    elif op == 2:
        print('A multiplicação entre {} e {} é {}'.format(v1, v2, v1*v2))
    elif op == 3:
        if v1 == v2:
            print('Não há maior pois os dois valores são equivalentes')
        elif v1 > v2:
            print('Entre {} e {} o maior valor é {}'.format(v1, v2, v1))
        else:
            print('Entre {} e {} o maior valor é {}'.format(v1, v2, v2))
    elif op == 4:
        v1 = int(input('Digite novamente o primeiro valor: '))
        v2 = int(input('Digite novamente o segundo valor: '))
    elif op != 5:
        print('Inserção inválida, digite um valor válido!')
print('Obrigado! Tenha um ótimo dia!')

# Resolução do professor

from time import sleep

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0

while opcao != 5:
    print('''
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa
        ''')
    opcao = int(input('>>>>>> Qual é sua opção: '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}'.format(n1, n2, soma))
    elif opcao == 2:
        produto =  n1 * n2
        print('O resultado de {} x {} é {}'.format(n1, n2, produto))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
    elif opcao == 4:
        print('informe os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando ...')
    else:
        print('Opção inválida. Tente novamente')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa! Volte Sempre!')