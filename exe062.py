# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra 
# quando ele disser que quer mostrar 0 termos.


p1 = int(input('Digite o primeiro termo da P.A: ')) 
r = int(input('Digite a razão da P.A: '))
termo = p1
count = 1


total = 0
novos_termos = 10
contador = novos_termos

print('Os 10 primeiros termos da P.A são: ')
while novos_termos != 0:
    total = total + novos_termos
    while count <= total:   
            print('{} > '.format(termo), end='')
            termo += r
            count += 1
    print('FIM')
    novos_termos = int(input('Digite a nova quantidade de termos ou digite 0 para sair do programa: '))
    contador += novos_termos
print('Você visualizou {} termos'.format(contador))

# Resolução do professor

print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} > '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados'.format(total))
