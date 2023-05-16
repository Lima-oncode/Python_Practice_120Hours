# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular
# (largura e comprimento) e mostre a área do terreno.

def area():
    print()
    pri = ('Calcule a área do terreno')
    print(pri)
    print(len(pri) * '-')
    comp = float(input('Digite o comprimento do terreno (m): '))
    larg = float(input('Digite a largura do terreno (m): '))
    calc_area = comp * larg
    print(f'O comprimento do terreno é {comp} e sua largura é {larg} portanto o terreno tem {calc_area}(m²)')
    
area()

# Segunda forma de resolução pessoal

def area1(comp, larg):
    print()
    pri = ('Calcule a área do terreno')
    print(pri)
    print(len(pri) * '-')
    calc_area = comp * larg
    print(f'As dimensões do terreno são {comp} x {larg} portanto o terreno tem {calc_area}(m²)')

comprimento = float(input('Comprimento do terreno: '))  
largura = float(input('Largura do terreno: '))  
area1(comprimento, largura)
    

# Resolução do professor

def área(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {a}m²')
 

print(' Controle de Terrenos ')
print('-' * 20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
área(l,c)
