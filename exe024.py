'''Crie um programa que leia o nome de uma cidade e diga se ela começa ou nao com o nome
'SANTO.'''


#Minha resolução:

cidade = input('Digite o nome da cidade: ')
cidade_existe = (cidade[:5].upper() == 'SANTO')

if cidade_existe == False:
    print ('Santo nao existe no primeiro nome desta cidade')
else:
    print ('O nome desta cidade começa com santo')

#Resolução do professor

# O Strip após o input remove os espaços caso o usuário digite a string com espaços
cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO') 


    
