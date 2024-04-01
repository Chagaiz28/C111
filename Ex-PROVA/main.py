import numpy as np

arr = np.loadtxt('paises.csv', delimiter=';', dtype = str, encoding='utf-8', skiprows=1)

# Q1
slicing = arr[:, [0, 1, 2, 3]]
print(slicing)

# Q2

regioes = np.unique(arr[:, 1])
print(regioes)

# Q3
literacy = np.mean(arr[:, 9].astype(float))
print(f'Taxa média de alfabetização: {literacy:.2f}')

# Q4

stripped_regions = np.char.strip(arr[:, 1])

norte_america = np.count_nonzero(stripped_regions == 'NORTHERN AMERICA')

print(f'Número de países da América do Norte: {norte_america}')

# Q5

south_america = arr[stripped_regions == 'LATIN AMER. & CARIB']
gdp = south_america[:, 8].astype(float)
max_gdp = np.argmax(gdp)
country = south_america[max_gdp, 0]
print(f'País da América do Sul e Caribe com maior renda per capita: {country}')