km = float(input('Digite quantos KM foi rodado com o veículo'))
dias = int(input('Digite quantos dias o veículo foi utilizado'))
valorkm = km*0.15
valordia = dias*60
total = valorkm + valordia
print('O valor total da locação é R${:.2f}.\t Sendo R${:.2f} referente a quilometragem.\t R${:.2f} referente aos dias'.format(total,valorkm,valordia))