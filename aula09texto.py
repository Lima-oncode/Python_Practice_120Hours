'''para textos longos no print usar aspas 3 vezes
frase = 'Curso em vídeo python'
print(frase.count('o'))
frase = 'Curso em vídeo python'
print(frase.upper().count('O'))'''

'''frase = 'Curso em vídeo python'
print(frase[:21])

frase = '  Curso em vídeo python  '
print(len(frase))

frase = '  Curso em vídeo python  '
print(len(frase.strip()))

frase = 'Curso em vídeo python'
frase = print(frase.replace('python','android'))
print(frase)'''

'''frase = ('Curso em Vídeo Python')
print('Curso' in frase)
print(frase.find('Curso'))
print(frase.find('Vídeo'))
print(frase.find('video'))'''

frase = ('Curso em Vídeo Python')
print(frase.lower().find('vídeo'))

frase = ('Curso em Vídeo Python')
dividido = (frase.split())
print(dividido[2][3])