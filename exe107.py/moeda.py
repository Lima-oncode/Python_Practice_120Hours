def metade(n):
    return n / 2

def dobro(n):
    return n * 2

def aumentar(n, porcento):
    valor = n / 100 * porcento
    valorfinal = n + valor
    return valorfinal

def diminuir(n, porcento):
    valor = n / 100 * porcento
    valorfinal = n - valor
    return valorfinal

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