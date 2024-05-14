import pandas as pd
# Q1-A
df = pd.read_csv('paises.csv', delimiter=';')
oceania = 'Oceania'.strip().lower()

df['Region'] = df['Region'].str.strip().str.lower()

paises_oceania = df[df['Region'] == oceania]
nome_paises = paises_oceania['Country']
print(nome_paises)

# Q1-B
quantidade_paises = len(nome_paises)
print(quantidade_paises)

# Q2
media_literacy = df['Literacy (%)'].mean()
print(media_literacy)

# Q3
maior_populacao = df[df['Population'] == df['Population'].max()]
print(maior_populacao[['Country', 'Region']])

# Q4
paises_sem_costa = df[df['Coastline (coast/area ratio)'] == 0]
nome_paises_sem_costa = paises_sem_costa['Country']
nome_paises_sem_costa.to_csv('noCoast.csv', index=False)

