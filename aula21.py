# # Funções - Parte 2

# from random import randint
# Interactive Help / Ajuda Interativa
# Função Help()

# No terminal digite 'python' e prossiga digitando help()
# num arquivo .py podemos chamar a função help passando a função que tem dúvida como parametro:

help(print)
help(len)

# ou usando o __doc__:

print(input.__doc__)

# Docstrings - Para usarmos help para uma função nova criada podemos documentar seus parâmetros
# e funcionamentos



# def contador(i, f, p):
#     """
#     -> Faz uma contagem e mostra na tela.
#     :param i: Início da contagem
#     :param f: Fim da contagem
#     :param p: Passo de contagem
#     :return: Sem retorno
#     """
#     c = i
#     while c <= f:
#         print(f'{c}', end='..')
#         c += p
#     print('Fim!')

# contador(2,10,2)
# help(contador)

# # Parâmetros Opcionais

# def somar(a, b, c):
#     s = a + b + c
#     print(f'A soma vale {s}')
    
# # Nesta soma daria certo pelo fato de ter os 3 parmetros solicitados
# somar(3,2,5)

# # Neste caso daria erro devido haver somente 2 parâmetros
# somar(8, 4)

# # Os parâmetros opcionais seria funcional para este caso uma vez que definimos um valor padrão/opcional:
# # Sendo indiferente se passamos os 3, 2 ou 1 valor(es)
# def somar(a=0, b=0, c=0):
#     s = a + b + c
#     print(f'A soma vale {s}')
    
# Escopo de variáveis:
# Neste caso a variável 'a' que é definida fora da função e depois da função é uma variável de escopo
# global. Reconhecida pela função mesmo definida após a def.

# O 'b' e o 'c' são variáveis de escopo local. variáveis locais só são reconhecidas na função onde ela 
# foi criada. Neste exemplo 'b' recebe o valor da global 'a' e soma com + 4 se tornando 9 invés de 5. 
# Porém, 'a' ainda vale 5

def teste(b):
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')
    
a = 5
teste(a)
print(f'A fora vale {a}')

# É possível criar uma váriavel de escopo local mesmo existindo uma de escopo global, confira o 'a':
# dentro da função o 'a de escopo local' toma a posição do 'a de escopo global' porém 'b' ainda é um
# clone do escopo global

def teste(b):
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')
    
a = 5
teste(a)
print(f'A fora vale {a}')

# É possível tornar uma variável de escopo local para uma global mesmo estando em uma função:
# Neste formato tanto o 'a dentro' dentro como 'a fora' valem 8, perdendo o valor 5 definido no programa
# principal

def teste(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')
    
    
a = 5
teste(a)
print(f'A fora vale {a}')

# Retornando valores - return
# invés de printar o retorno de cada vez que a def é chamada: print(f'A soma vale {s}')
# usaremos o return s no lugar
 

def somar(a=0, b=0, c=0):
    s = a + b + c
    return s
    
r1 = somar(3, 2, 5)    
r2 = somar(2,2)
r3 = somar(6)

print(f'Os resultados foram {r1}, {r2}, {r3}')


# Exercício exemplo 1:

def fatorial(num):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial(1)
print(f'Os resultados são {f1}, {f2} e {f3}')

# Exercício exemplo 2:

def parouimpar(n=0):
    if n % 2 == 0:
        return True
    else:
        return False
    
num = int(input('Digite um número: '))
if parouimpar(num):
    print('É par!')
else:
    print('Não é par!')
    




