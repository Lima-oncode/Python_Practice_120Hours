from datetime import date
import csv

dt = date.today()
dt = dt.strftime("%d/%m/%Y")
filename = "test.csv"
exp = []
stopped = False

with open(filename, 'w') as file:
    csvwriter = csv.writer(file)
    while not stopped:
        xp = int(input("Qual o valor da sua despesa? (Digite 0 para parar): "))
        if xp == 0:
            stopped = True
        else:
            csvwriter.writerow([dt, xp])
            exp.append(xp)
file.close()
print(f'Suas despesas hoje foram {exp}')
print(f'O total de despesas foi {sum(exp)}')