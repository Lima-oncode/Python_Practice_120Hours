'''Faça um programa que leia um ângulo qualquer e mostre na tela o valor de seno, cosseno
e tangente desse ângulo [vale ressaltar que o angulo da variável está em graus centígrados.
Deste modo é necessário realizar a conversão para radianos] '''

from math import radians,sin,cos,tan
ang = int(input('Digite o valor do ângulo'))
sen = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))
print('ângulo {}º, seno {:.2}, cosseno {:.2}, tangente {:.2}'.format(ang,sen,cos,tan))