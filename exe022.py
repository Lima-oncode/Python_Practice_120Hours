'''Crie um programa que leia o nome completo de uma pessoa e mostre:
1 - O nome com todas as letras maisculas
2 - O nome com todas as letras minusculas
3 - Quantas letras ao todo sem considerar os espaços
4 - Quantas letras tem o primeiro nome'''

# Realizando a tarefa onde a sintaxe se encontra dentro do print

#nome = input('Digite o seu nome completo: ')

# 1
#print(nome.upper())

# 2
#print(nome.lower())

# 3
#print(len(nome.strip()))

# 4
#print(len(nome.split()[0]))

# Realizando a tarefa com os métodos dentro das variáveis
'''Crie um programa que leia o nome completo de uma pessoa e mostre:
1 - O nome com todas as letras maisculas
2 - O nome com todas as letras minusculas
3 - Quantas letras ao todo sem considerar os espaços
4 - Quantas letras tem o primeiro nome

nome = str(input('Digite o seu nome completo: ')) 
mai = nome.upper()
min = nome.lower()
qtd_total_name = len(nome.strip())
qtd_first_name = len(nome.split()[0])

print('O seu nome completo em maiúsculas é {}'.format(mai))
print('O seu nome completo em minúsculas é {}'.format(min))
print('O seu nome completo tem {} letras'.format(qtd_total_name))
print('O seu primeiro nome tem {} letras'.format(qtd_first_name))'''


# resolução professor
# em correção a minha solução que contou em qtd_total_name os espaços de dentro, 
# o strip na string inputada e o - variavel.count('espaço') 

nome = str(input('Digite seu nome: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome inteiro sem espaços tem {} caracteres'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} caracteres'.format(nome.find(' ')))

#outra forma de fazer o passo 4

separa = (nome.split())
print('Seu primeiro nome é {} e tem {} caracteres'.format(separa[0], len(separa[0])))



""""
frase = 'Curso em Vídeo Python'

print(frase)

''' Fatiamento '''

print(frase[9:14])

print(frase[9:21:2])

print(frase[:5])

print(frase[15:])

print(frase[9::3])

''' Análise '''

print(len(frase))

print(frase.count('o'))

print(frase.count('o',0,13))

print(frase.find('deo'))

# O retorno -1 como resultado de find() significa que a string não foi encontrada
print(frase.find('Android'))

# O retorno de (string in frase) é um bool de True para verdadeiro e False para falso 
print('Curso' in frase)

''' Transformação '''

# O replace é usado para trocar um caracter por outro
print(frase.replace('Python', 'Android'))

# Lembre se de que métodos do python usam parenteses vazios / o método upper torna a string maiuscula
print(frase.upper())

# Assim como o upper, o lower é um método portanto use o () / o método lower torna a string minuscula
print(frase.lower())

# Torna a string inteira para minúsculo e maiusculo somente a primeira letra
print(frase.capitalize())

# Torna as string minuscula porém a cada espaço identificado ele torna a primeira letra maiuscula
print(frase.title())

frase1 = '   Aprenda Python   '

print(frase1)

# Remove espaços desnecessários, tanto á esquerda quanto á direita 
print(frase1.strip())

# Remove espaços denecessários á direita
print(frase1.rstrip())

# Remove espaços denecessários á esquerda
print(frase1.lstrip())

''' Divisão '''

# Gera uma lista para cada palavra na cadeia de caracter colocada na variável
print(frase.split())

''' Junção '''

# O split realiza a junção de cada elemento apontados, no caso se tivermos as palavras separadas em listas
#com o split, podemos fazer o join colocando algum outro caracter para dividi-los

juncao = frase.split()
print('-'.join(juncao))

print(frase.split(('-'.join(frase))))


''' Recapitulando '''

# Lembrando que para o python tudo é um objeto. podemos colocar frase.método.método
print(frase.upper().count('O'))

# len faz a contagem de caracteres porém o strip retira os espaços desnecessários.
print(len('   Curso em vídeo Python   '.strip()))

# Replace realizando a troca de palavras na string, porém (somente nesta instancia)
print(frase.replace('Python', 'Android'))

# Apesar de ter sido realizado o replace, uma string é imutável. A nao ser que colocassemos a linha de código
# onde está o replace em uma nova variável
print(frase)

# retornando um bool se a string existir na variável
print('Curso' in frase)

# Mostra em qual posição foi encontrado a string referenciada
print(frase.find('Curso'))

# String tranformada para minusculo retornando a posicao onde a palavra em minusculo foi encontrada
print(frase.lower().find('vídeo'))

# Foi criada uma variável para guardar a string splitada e printar somente a palavra da posicao 0
dividido = frase.split()
print(dividido[0])

# A variável está pegando a segunda palavra da string e trazendo o caracter da posicao 3
print(dividido[2][3])"""










