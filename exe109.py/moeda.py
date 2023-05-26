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