def metade(n, formatado=False):
    res = n / 2
    return res if formatado == False else moeda(res)

def dobro(n, formatado=False):
    res = n * 2
    return res if formatado == False else moeda(res)

def aumentar(n, porcento, formatado=False):
    res = n + (n / 100 * porcento)
    return res if formatado == False else moeda(res)

def diminuir(n, porcento, formatado=False):
    res = n - (n / 100 * porcento)
    return res if formatado == False else moeda(res)

def moeda(n, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')

def resumo(valor = 0, taxa_a = 10, taxa_d = 5):
    print('-' * 40)
    print('RESUMO DO VALOR'.center(40))
    print('-' * 40)
    print(f'Preço analisado: \t{moeda(valor)}')
    print(f'Dobro do preço: \t{dobro(valor, True)}')
    print(f'Metade do preço: \t{metade(valor, True)}')
    print(f'{taxa_a}% de aumento: \t{aumentar(valor, taxa_a, True)}')
    print(f'{taxa_d}% de redução: \t{diminuir(valor, taxa_d, True)}')
    print('-' * 40)

# Resolução do professor

def aumentar2(preco, taxa, formatado=False):
    res = preco + (preco * taxa/100)
    return res if formatado == False else moeda2(res)

def diminuir2(preco, taxa, formatado=False):
    res = preco - (preco * taxa/100)
    return res if formatado == False else moeda2(res)

def dobro2(preco, formatado=False):
    res = preco * 2
    return res if formatado == False else moeda2(res)

def metade2(preco, formatado=False):
    res = preco / 2
    return res if formatado == False else moeda2(res)

def moeda2(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')

def resumo2(preco = 0, taxaa = 10, taxar = 5):
    print('-' * 40)
    print('RESUMO DO VALOR'.center(40))
    print('-' * 40)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preco, taxaa, True)}')
    print(f'{taxar}% de redução: \t{diminuir(preco, taxar, True)}')
    print('-' * 40)