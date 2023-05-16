# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá
# analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

lista = []
expressao = str(input('Digite a expressão: '))
for caracter in expressao:
    if caracter == '(':
        lista.append(caracter)
    elif caracter == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) > 0:
    print('Está faltando parênteses na expressão digitada')
else:
    print('A expressão está com os parênteses fechados na ordem')

# Resolução do professor

expr = str(input('Digite a expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')