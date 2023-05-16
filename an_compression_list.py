# Primeiro uma loop for normal e depois utilizando compreensão de lista

# l = []
# for num in range(100):
# 	l.append(num) 

# Agora utilizando uma compreensão de lista
l  = [num for num in range(100)]
#print(l)

par = [num * 2 for num in range(50)]
#print(par)

numero = int(input('Qual número deseja ver a tabuada: '))
tab = [(x + 1) * numero for x in range(20)]
print(tab)

tab2 = [str(x+1) + ' x ' + str(numero) + ' = '+ str((x+1)*numero) for x in range(10)]
print(tab2)

tab3 = [f'{x+1} x {numero} = {(x+1) * numero}' for x in range(10)]
print(tab3)