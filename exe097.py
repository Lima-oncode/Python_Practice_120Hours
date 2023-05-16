# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro
# e mostre uma mensagem com tamanho adaptável.

def escreva(msg):
    print('-' * len(msg)) 
    print(msg)
    print('-' * len(msg))
    
escreva('olá bom dia, tudo bem com você')

# Resolução do professor

def escreva1(msg):
    tam = len(msg)+4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    
    

# Programa Principal
escreva1('Curso em vídeo')    