# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique
# o número a calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado
# ou não na tela o processo de cálculo do fatorial.

def fatorial(n):
    '''
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :return : O valor do Fatorial de um número n.
    '''
    from math import factorial
    return factorial(n)
    
# Resolução do professor

def fatorial1(n, show=False):
    '''
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (parâmetro opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    '''
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(f' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

num = int(input('Digite um número para ver seu fatorial: '))
print(fatorial1(num, True))
    