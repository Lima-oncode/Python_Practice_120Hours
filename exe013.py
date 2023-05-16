s = float(input('digite o valor do salário'))
s1= (s*15/100)
a = (s+s1)
print('Seu novo salário é R${:.2f}, com aumento de R${:.2f}'.format(a,s1))