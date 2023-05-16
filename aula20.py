# Funções - Parte 1
# As funções podem ser utilizadas para automatizar rotinas usadas muitas vezes no código em diferentes 
# momentos

# # Exemplo 1:
def mostralinha():
    print('---------------------------------')
    
# # Podemos usar a função criada acima invés de digitar print repetidas vezes:
# # Sempre que a função é chamada ela é executada

mostralinha()   
print('    Sistema de alunos    ')
mostralinha()
mostralinha()
print('    Cadastro de funcionários    ')
mostralinha()
mostralinha()
print('    Sistema de alunos    ')
mostralinha()

# # Exemplo 2:

def lin():
    print('-' * 30)
    
    
lin()
print('   Curso em vídeo   ')
print('   Aprenda Python   ')
print('   Lucas Lima   ')
lin()

# Exemplo 3:
# Quando colocamos um parametro na definição da função podemos definir ele/alterar seu valor na hora de
# chamar a função como no caso da função mensagem. O valor do parametro msg foi definido em mensagem('')

def mensagem(msg):
    print('------------------------------')
    print(msg)
    print('------------------------------')
    
mensagem('Sistema de alunos')

def titulo(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)
    
titulo('Curso em vídeo')
titulo('Aprenda Python')
titulo('Lucas Lima')

# Exemplo 4:
def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = (a + b)
    print(f'A soma A + B = {s}')

soma(4, 5)
soma(8, 9)
soma(2, 1)
soma(a=100, b=100)
soma(b=200, a=250)

# Exemplo 5:
# Empacotando parâmetros

def contador(*num):
    print(num)

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

# # Exemplo 6:

def contador(*num):
    for valor in num:
        print(valor)

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

# # Exemplo 7:

def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números')

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

# Exemplo 8:
# Função para dobrar o valor de uma estrutura composta no caso uma lista. desta forma a função dobraria
# os valores do vetor

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
    print(lst)
        
valores = [5,5,5,3,9,2]
dobra(valores)