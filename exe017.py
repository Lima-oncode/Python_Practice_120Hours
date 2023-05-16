# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um
#triângulo retângulo, calcule  e mostre o comprimento da hipotenusa.
import math
co = float(input('Entre com o valor do cateto oposto'))
ca = float(input('Entre com o valor do cateto adjacente'))
comp = (math.pow(co,2) + math.pow(ca,2))
hip = math.pow(comp,1/2)
print('Com base no cateto oposto {:.1f} e adjacente {:.1f} o comprimento da hipotenusa é {:.1f}'.format(co,ca,hip))

'''Método 1 do proff:
hi = (co ** 2 + ca ** 2) ** (1/2)'''

'''Método 2 do proff:
hi = math.hypot(co,ca)'''



