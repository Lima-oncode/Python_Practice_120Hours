# Crie um código em python que teste se o site Pudim está acessível pelo computador usado.

import urllib 
import urllib.request

try:
    site = urllib.request.urlopen('https://docs.python.org/3/library/urllib.parse.html#module-urllib.parse')
except urllib.error.URLError:
    print('O site não está acessível no momento.')
else:
    print('Deu certo, o link da página está funcionando!')
    # print(site.read())

