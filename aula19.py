# Dicionários
# Podemos criar uma váriavel composta do tipo dicionário das seguintes maneiras:

# Conceito

#dados = dict()
dados = {'nome':'Pedro', 'idade':'25' }

# Neste caso, o valor output será 'Pedro' devido a referência da chave 'nome'
print(dados['nome'])

# Adicionando dados em dicionários passando nome da nova chave '= valor'
dados['sexo'] = 'M'
print(dados)

# Eliminando elementos
del dados['idade']

# Métodos:

filme = {'título':'StarWars',
         'ano':1977,
         'diretor':'GeorgeLucas'}

# values() - método para pegar somente os valores do dicionário
print(filme.values())

# keys() - método para pegar somente as chaves do dicionário
print(filme.keys())

# items() - método para pegar tanto as chaves quantos os valores do dicionário
print(filme.items())

# Exemplos:

# laço utilizando método items():
for k, v in filme.items():
    print(f'o {k} é {v}')

# Uso de dicionários dentro de listas:
locadora = [{'título':'StarWars',
            'ano':1977,
            'diretor':'GeorgeLucas'},
            {'título':'Avengers',
            'ano':2012,
            'diretor':'JossWhedon'},
            {'título':'Matrix',
            'ano':1999,
            'diretor':'Wachowski'}]

print(locadora[0]['ano'])
print(locadora[1]['ano'])
print(locadora[2]['ano'])

pessoas = {'nome':'Lucas',
           'sexo':'M',
           'idade':'22'}

print(pessoas)
print(pessoas['nome'])
print(pessoas['idade'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')

for k in pessoas.keys():
    print(k)
    
for v in pessoas.values():
    print(v)

pessoas['nome'] = 'Fulano'
pessoas['peso'] = '98.5'

for k, v in pessoas.items():
    print(f'{k} = {v}')

# Exemplo - Adicionando dicionários a uma lista vazia

Brasil = []    
estado1 = {'uf':'Rio de Janeiro', 'sigla':'RJ'}
estado2 = {'uf':'São Paulo', 'sigla':'SP'}
Brasil.append(estado1)
Brasil.append(estado2)
print(Brasil)
print(Brasil[0])
print(Brasil[1])
print(Brasil[0]['uf'])
print(Brasil[1]['uf'])

# Exemplo - Inputando os valores de um dict em um laço e adicionando a uma lista vazia a cada iteração
# Método copy() - Método interno de dicionários para copiar os dados a cada iteração
brasileiro = []
estado = {}
for x in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasileiro.append(estado.copy())
print(brasileiro)
for dic in brasileiro:
    for k, v in dic.items():
        print(f'O cammpo {k} tem o valor {v}')
     