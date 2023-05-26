# Dentro do pacote utilidadescev que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função input(), mas com uma validação de dados para aceitar apenas valores que sejam monetários.

from utilidadescev import moeda, dados
from colorama import Style, Fore

p = dados.leiadinheiro(Style.BRIGHT + Fore.GREEN + 'Digite o preço: R$')
moeda.resumo(p)
