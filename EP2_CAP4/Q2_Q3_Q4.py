import numpy as np

np.random.seed(10)

mtz = np.random.randint(1, 50, 16).reshape(4, 4)

print("Matriz:")
print(mtz)

media_linhas = np.mean(mtz, axis=1)
print("\nMédia de cada linha:")
print(media_linhas)

media_colunas = np.mean(mtz, axis=0)
print("\nMédia de cada coluna:")
print(media_colunas)

maior_media_linha = np.max(media_linhas)
maior_media_coluna = np.max(media_colunas)

print(f"\nMaior média de linha: {maior_media_linha}")
print(f"Maior média de coluna: {maior_media_coluna}")

valores, contagens = np.unique(mtz, return_counts=True)
aparicoes = dict(zip(valores, contagens))
print("\nQuantidade de aparições de cada número:")
print(aparicoes)

numeros_com_2_aparicoes = [numero for numero, quantidade in aparicoes.items() if quantidade == 2]
print("\nNúmeros que aparecem duas vezes:")
print(numeros_com_2_aparicoes)