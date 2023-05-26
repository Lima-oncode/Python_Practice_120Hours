# Erros e Exceções

# Exemplo 1 

# print(x)

# Devido a variável x ele retorna 'NameError' que chamamos de exceção ou except.    
#-----------------------------------------------------------------------------------------------------------

# Exemplo 2

# n = int(input('num: '))
# print(f'Você digitou o número {n}')

# Caso digite oito ao invés do inteiro 8 ele retornará um ValueError que também é uma exceção

#-----------------------------------------------------------------------------------------------------------

# Exemplo 3

# a = int(input('Numerador: '))
# b = int(input('Denominador: '))
# r = a/b
# print(f'O resultado é {r}')

# caso no denominador o valor seje 0 ele retornará  ZeroDivisionError que é uma exceção para quando algum número for dividido por zero

#-----------------------------------------------------------------------------------------------------------

# Exemplo 4

# a = 2/'2'

# Neste exemplo o python retornará a exceção 'TypeError' que se refere a erros de tipagem uma vez que a variável está tentando fazer uma operação de um inteiro com uma string

#-----------------------------------------------------------------------------------------------------------

# Exemplo 5

# lst = [3,4,5]
# print(lst[3])

# Neste exemplo o python retornará a exceção 'IndexError' que se refere a quarta posição da lista uma vez que a mesma possui somente 3 dados nos índices '0,1,2'

#-----------------------------------------------------------------------------------------------------------

# Try e Except

# Try - Tente fazer alguma coisa
# Except - Se eu tentar fazer algo no Try e falhar o Except entra

#-----------------------------------------------------------------------------------------------------------

# Exemplo 6

# try:
#     a = int(input('Numerador: '))
#     b = int(input('Denominador: '))
#     r = a/b
# except Exception as erro:
#     print(f'O problema entrado foi {erro.__class__}')
# else:
#     print(f'O resultado é {r}')
# finally:
#     print('Volte sempre! Muito obrigado!')
    
    
# Exemplo 6

# try:
#     a = int(input('Numerador: '))
#     b = int(input('Denominador: '))
#     r = a/b
# except (ValueError, TypeError):
#     print(f'Tivemos um problema com os tipos de dados que você digitou.')
# except ZeroDivisionError:
#     print('Não é possível dividir um número por zero')
# except KeyboardInterrupt:
#     print('O usuário não preferiu informar os dados!')
# except Exception as erro:
#     print(f'O erro encontrado foi {erro.__cause__}')
# else:
#     print(f'O resultado é {r}')
# finally:
#     print('Volte sempre! Muito obrigado!')
