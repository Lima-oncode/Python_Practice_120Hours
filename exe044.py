# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal
# e condição de pagamento:
# - À vista dinheiro/cheque: 10% de desconto
# - À vista no cartão: 5% de desconto
# - Em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros

preco = float(input('Digite o valor do produto: R$ '))
a_vista = preco - (preco * 10 / 100)
a_vista_cartao = preco - (preco * 5 / 100)
parcelado = preco + (preco * 20 / 100)


print('''
=================== Escolha sua forma de pagamento ======================
[ 1 ] - A vista dinheiro/cheque com 10% de desconto no valor do produto.
[ 2 ] - A vista no cartão com 5% de desconto no valor do produto.
[ 3 ] - Em até 2x no cartão mantendo o preço normal do produto.
[ 4 ] - 3x ou mais no cartão com 20% de juros.
''')
condicao = int(input(': '))

if condicao == 1:
    print('''Você pagou a sua compra a vista, portanto ganhou um desconto de 10%
O valor inicial de R${:.2f} caiu para R${:.2f} garantindo um desconto de R${:.2f} do total'''
    .format(preco, a_vista, preco - a_vista))

elif condicao == 2:
    print('''Você pagou a sua compra a vista no cartao, portanto ganhou um desconto de 5%
O valor inicial de R${:.2f} caiu para R${:.2f} garantindo um desconto de R${:.2f} do total'''
    .format(preco, a_vista_cartao, preco - a_vista_cartao))

elif condicao == 3:
    parcelas = preco/2
    print('''O produto sairá no preco normal de {}. Você irá pagar {} parcelado em 2x de R${}'''
    .format(preco, preco, parcelas))

elif condicao == 4:
    vezes = int(input('Você deseja parcelar quantas vezes? '))
    parcelas = parcelado / vezes
    print('''O produto custa R${:.2f} porém a compra parcelada resulta em 20% de juros. 
Você irá pagar R${:.2f} parcelado em {:.0f}x de R${:.2f}'''.format(preco, parcelado, vezes, parcelas ))

else:
    print('Opção inválida! escolha uma opção válida.')


# Resolução do professor

print('{:=^40}'.format(' LOJAS GUANABARA '))
preco = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] á vista dinheiro/cheque
[ 2 ] á vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))

if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totparc, parcela))
else:
    total = 0
    print('Opção inválida. Tente novamente!')
print('Sua compra de R${} vai custar R${} no final.'.format(preco, total))
