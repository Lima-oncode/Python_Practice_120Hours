#  Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento
# de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO (< 18 anos),
# OPCIONAL (> 65 anos) ou OBRIGATÓRIO (> 18 and < 65) nas eleições.

def voto(ano_n):
    from datetime import date
    dt = date.today().year
    idade = dt - ano_n
    print('=-' * 15, 'Verificador de voto obrigatório', '=-' * 15)
    if idade >= 18 and idade < 65:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'
    elif idade < 18:
        return f'Com {idade} anos: NÃO VOTA.'
    else:
        return f'Com {idade} anos: VOTO OPCIONAL'
    
print('-' * 25)
nascimento = int(input('Em que ano você nasceu? '))
print(voto(nascimento))


# Resolução do professor

# Escopo de importação - podemos usar a importação somente dentro da função, ecomizando memória. A classe
# importada só funcionará dentro da função e não no código inteiro

def voto1(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade >= 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'    

# Programa principal
nasc = int(input('Em que ano você nasceu? '))
print(voto1(nasc))
