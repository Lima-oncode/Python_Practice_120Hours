# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar
# para cada palavra, quais são as suas vogais.

palavra = ('martelo', 'mouse', 'teclado')

for x in palavra:
    print(f'\nNa palavra {x} temos as vogais ', end='')
    for letra in x:
        if letra.lower() in 'aeiou':
            print(f'[{letra}]', end=' ')

# Resolução do professor

palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar', 
            'trabalhar', 'mercado', 'programador', 'futuro')

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end='')
