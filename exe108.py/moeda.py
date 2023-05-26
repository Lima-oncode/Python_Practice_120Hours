def metade(n):
    res = n / 2
    return res

def dobro(n):
    res = n * 2
    return res

def aumentar(n, porcento):
    res = n + (n / 100 * porcento)
    return res

def diminuir(n, porcento):
    res = n - (n / 100 * porcento)
    return res

def moeda(n, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')

# Resolução do professor

def aumentar2(preco, taxa):
    res = preco + (preco * taxa/100)
    return res

def diminuir2(preco, taxa):
    res = preco - (preco * taxa/100)
    return res

def dobro2(preco):
    res = preco * 2
    return res

def metade2(preco):
    res = preco / 2
    return res

def moeda2(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')