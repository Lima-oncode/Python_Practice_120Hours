n = input('Digite algo:')
# print('o tipo primitivo desse valor é:', (type(n)))
# print('É um número?',n.isnumeric())
# print('só tem espaço?',n.isspace())
# print('É alfabético?',n.isalpha())
# print('É alfanumérico?',n.isalnum())
# print('Está em maiúsculas?',n.isupper())
# print('Está em minusculas?',n.islower())
# print('Está capitalizada?',n.istitle())

# Segunda resolução usando o .format

énumerico = n.isnumeric()
éespaço = n.isspace()
éalfanumerico = n.isalnum() 

print('É número? {}'.format(énumerico))
print('É espaço? {}'.format(éespaço))      
print('É alfanumérico {}'.format(éalfanumerico))
print('Resolução dos dados {} {} {} '.format(énumerico, éespaço, éalfanumerico))




