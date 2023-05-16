#how to make program excel reading in python?

# df = {}
# df = df.append(pd.read_excel(file.xlsx), ignore_index=True)
# df_2 = pd.read_excel(file)

# #Concatenando as duas planilhas excel
# df = pd.concat([df, df_2], ignore_index=True)

import pandas as pd

# A leitura do arquivo excel necessita de seu caminho absoluto
df1 = pd.read_excel('C:/Users/BlueShift/Desktop/FMQ/ARQUIVOS_FQM_RX/fqm_2022_01_fqm-estrutura_1964 (3).xlsx')
print(df1)



