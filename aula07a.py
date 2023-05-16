#+ Adição 5+2==7
#- Subtração 5-2==3
#* Multiplicação 5*2==10
#/ Divisão 5/2==2.5 (float)
#**Potencialização 5**2 (5*5)==25
#//Divisão inteira 5/2 ==2 e sobra 1
#% Resto da divisão 5%2==1

#Ordem de precedência/qual é realizado primeiro
#1º ()
#2º **
#3º * / // % (se tiver eles juntos faz quem aparecer primeiro
#4º +-
#Exemplos
#5+3*2==11
#3*5+4**2==31
#3*(5+4)**2==243
#Raiz quadrada == criar a potencia de um numero por meio é o mesmo que raiz quadrada
#Ex: 25**1/2 == 5.0
#Raiz cubica == criar a potencia de um numero por 1/3
#Ex: 125**1/3

#x = input('Qual é o seu nome?')
#print('Prazer em te conhecer {:20}!'.format(x))

#x = input('Qual é o seu nome?')
#print('Prazer em te conhecer {:20}!'.format(x))  #neste formato ele usou os 20 espaços
#Qual é o seu nome?lucas
#Prazer em te conhecer lucas               !

#x = input('Qual é o seu nome?')
#print('Prazer em te conhecer {:>20}!'.format(x)) #Neste caso ocorre o alinhamento a direita
#Qual é o seu nome?Lucas
#Prazer em te conhecer                Lucas!

#x = input('Qual é o seu nome?')
#print('Prazer em te conhecer {:<20}!'.format(x)) #Neste caso ocorre o alinhamento a esquerda
#Qual é o seu nome?Lucas
#Prazer em te conhecer Lucas               !

#x = input('Qual é o seu nome?')
#print('Prazer em te conhecer {:^20}!'.format(x)) #Neste formato ocorre a centralização
#Qual é o seu nome?Larissa
#Prazer em te conhecer       Larissa       !

#x = input('Qual é o seu nome?')
#print('Prazer em te conhecer {:=^20}!'.format(x)) #Neste formato é centralizado com = em volta
#Qual é o seu nome?Lucas
#Prazer em te conhecer =======Lucas========!

n1 = int(input('Digite um valor'))
n2 = int(input('Digite outro valor'))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2
print('a soma vale {},o produto é {}, a divisão é {:.3f}, a divisão inteira é {}, a exponenciação é {}'.format(s,m,d,di,e), end='')

# \n é quebra de linha e end = '' é para a impressão ficar na mesma linha