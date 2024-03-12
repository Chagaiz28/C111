import numpy as np

# Questão 1
arr = np.linspace(0, 1, 21)
print("Array original:")
print(arr)

#Questão 2
arr_par1 = np.arange(0, 52, 2)
print("\nNúmeros pares de 0 a 50:")
print(arr_par1)

arr_par2 = np.arange(100, 49, -2)
print("\nNúmeros pares de 100 a 50:")
print(arr_par2)

arr_concatenado = np.concatenate((arr_par1, arr_par2))
print("Vetor concatenado:")
print(arr_concatenado)

#Questão 3
arr_descrescente = np.sort(arr_concatenado)[::-1]
print("\nVetor ordenado de forma decrescente:")
print(arr_descrescente)

#Questão 4
matriz = np.zeros((3, 4))
print("\nMatriz 3x4 de zeros:")
print(matriz)
matriz = matriz.reshape(-1)
print(matriz)

#Questão 5
matriz = np.ones((3, 4))
num_linhas, num_colunas = matriz.shape

total = num_colunas * num_linhas

if total % 2 == 0:
    print("\nA matriz é par")
else:
    print("\nA matriz é ímpar")
