def leiadinheiro(msg):
    from colorama import Style, Fore
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.')
        if entrada.isalpha() or entrada.strip() == '':
            print(Style.BRIGHT + Fore.RED + f'ERRO: {entrada} é um preço inválido!')
        else:
            valido = True
            return float(entrada)