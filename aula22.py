# MÓDULOS E PACOTES

# MODULARIZAÇÃO:
# - Surgiu no início da década de 60
# - Sistemas ficando cada vez maiores
# - Foco: Dividir um programa grande
# - Foco: Aumentar a legibilidade
# - Foco: Facilitar a manutenção
# - Para o python todo arquivo.py pode ser um módulo desde que tenha funções

# VANTAGENS
# - Organização do código
# - Facilidade na manutenção
# - Ocultação de código detalhado
# - Reutilização em outros projetos

# PACOTES
# O empacotamento pode ser feito colocando o arquivo .py dentro de uma pasta e cada função em um em uma nova pasta dentro da pasta main

from aula22module import fatorial, dobro, triplo
   
num = int(input("Digite um valor: "))

fat = fatorial(num)
dob = dobro(num)
tri = triplo(num)

print(f"O fatorial de {num} é {fat}")
print(f"O dobro de {num} é {dob}")
print(f"O triplo de {num} é {tri}")