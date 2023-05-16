# Crie um programa onde o usuário possa digitar cinco valores númericos e cadastre-os em uma lista 
# já na posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela

valores = []

for x in range(0, 5):
    num = int(input('Digite um valor: '))
    if x == 0:
        valores.append(num)
        print('Valor adicionado no final da lista')
    if x == 1:
        if num < valores[0]:
            valores.insert(0, num)
            print('valor adicionado na posição 0')
        else:
            valores.append(num)
            print('valor adicionado no final da lista')
    if x == 2:
        if num > valores[0] and num < valores[1]:
            valores.insert(1, num)
            print('valor adicionado na posicao 1')
        if num > valores[1]:
            valores.append(num)
            print('valor adicionado no final da lista')
        if num < valores[0]:
            valores.insert(0, num)
            print('valor adicionado na posicao 0')
    if x == 3:
        if num > valores[1] and num < valores[2]:
            valores.insert(2, num)
            print('valor adicionado na posicao 2')
        if num > valores[0] and num < valores[1]:
            valores.insert(1, num)
            print('valor adicionado na posicao 1')
        if num > valores[2]:
            valores.append(num)
            print('valor adicionado no final da lista')
        if num < valores[0]:
            valores.insert(0, num)
            print('valor adicionado na posicao 0')
    if x == 4:
        if num > valores[1] and num < valores[2]:
            valores.insert(2, num)
            print('valor adicionado na posicao 2')
        if num > valores[0] and num < valores[1]:
            valores.insert(1, num)
            print('valor adicionado na posicao 1')
        if num > valores[2] and num < valores[3]:
            valores.insert(3, num)
            print('valor adicionado na posicao 3')
        if num > valores[3]:
            valores.append(num)
            print('valor adicionado no final da lista')
        if num < valores[0]:
            valores.insert(0, num)
            print('valor adicionado na posicao 0')
    print(valores)
print(f'Os valores digitados foram {valores} na sequência menor para maior')

# Resolução do professor

lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram {lista}')