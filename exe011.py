alt = float(input('Digite a metragem da altura da parede'))
lar = float(input('Digite a metragem da largura da parede'))
area = (alt*lar)
lt = (area/2)

print('a dimensão da parede é {} x {} e sua área é {}m² metros e usará {} litros de tinta'
      .format(alt,lar,area,lt))