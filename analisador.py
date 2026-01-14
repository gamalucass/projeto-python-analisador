import pandas as pd

arquivo_csv = "dados.csv"
df = pd.read_csv(arquivo_csv)

print("\n Primeira linhas do arquivo CSV:")
print(df.head())

print("\n Estatisticas descritivas do arquivo CSV:")
print(df.describe())

print("\n Informacoes do DataFrame: ")
print(df.info())

print("\n Nomes das colunas do DataFrame: ")
print(df.columns.tolist())  


