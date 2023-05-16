# Listas parte 2
# Aula direcionada ao conhecimento de listas dentro de listas

# pessoas = [['Pedro', 25],['Maria', 19], ['João', 32]]

# print(pessoas[0][0]) # Pedro
# print(pessoas[1][1]) # 19
# print(pessoas[2][0]) # João
# print(pessoas[1]) # [Maria, 19]

teste = []
teste.append('Gustavo')
teste.append(40)

galera = []
galera.append(teste[:])
print(galera)
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

# O resultado é alterado devido o vínculo criado entre listas onde só é desfeito se for usado a cópia
# [:]

galera = [['João', 19],['Ana', 33],['Joaquim', 13],['Maria', 45]]
print(galera)
print(galera[0]) #Resultado do print: João, 19 (resultados da primeira lista dentro da lista main)
print(galera[0][0]) #Resultado do print: João (primeiro item dentro da primeira lista da lista main)
print(galera[2][1]) #Resultado do print: 13 (segundo item da terceira lista da lista main)

# Neste for é possível printar cada lista dentro da lista main
for x in galera:
    print(x)

# Neste for é possível printar o primeiro item das listas dentro da lista main
for x in galera:
    print(x[0])

# Neste for é possível printar o segundo item das listas dentro da lista main
for x in galera:
    print(x[1])
    
# Neste for é possível printar os itens das listas de forma formatada
for x in galera:
    print(f'{x[0]} tem {x[1]} anos de idade')

# Neste caso criamos um for com um range de 5 onde em cada iteração ele adiciona informações de input
# na lista dado e no final ele pegas todos os dados desta lista e passa para galera limpando a lista
# dado

galera = []
dado = []
totmai = totmen = 0

for c in range(0, 2):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1

print(f'Temos {totmai} pessoas maior de idade e {totmen} menor de idade')