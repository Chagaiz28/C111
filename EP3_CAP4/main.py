import numpy as np
# Q1
arr = np.loadtxt('space.csv', delimiter=';', dtype = str, encoding='utf-8', skiprows=1)

status = arr[:, -1]

num_success = np.count_nonzero(status == 'Success')

total_missoes = len(status)

porcentagem = (num_success / total_missoes) * 100

print(f'Porcentagem de missões bem sucedidas: {porcentagem:.2f}%')

# Q2
gasto = arr[:, -2].astype(float)

media_gasto = np.mean(gasto)

print(f'Média de gastos: {media_gasto:.2f}')

# Q3

loc = arr[:, 2]

missoesUSA = np.sum('USA' in l for l in loc)

print(f'Número de missões dos EUA: {missoesUSA}')

#Q4
missao_spacex = arr[arr[:, 1] == 'SpaceX']

custos_spacex = missao_spacex[:, -2].astype(float)

indice_missao_mais_cara = np.argmax(custos_spacex)

missao_mais_cara = missao_spacex[indice_missao_mais_cara]

print(f'Missão mais cara da SpaceX: {missao_mais_cara}')

#Q5
missao_especial_por_empresa = {}
for linha in arr:
    empresa = linha[1]
    if empresa in missao_especial_por_empresa:
        missao_especial_por_empresa[empresa] += 1
    else:
        missao_especial_por_empresa[empresa] = 1

print("Empresas que realizaram missões especiais:")
for empresa, quantidade in missao_especial_por_empresa.items():
    print(f"{empresa}: {quantidade} missões especiais")

