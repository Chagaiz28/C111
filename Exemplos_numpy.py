# NumPy
import numpy as np
'''
# Criando um NumPy Array
# 1-D
arr = np.array([1, 2, 3, 4])
print(arr)
print(type(arr))
# 2-D
mtz = np.array([[1, 2],[3,4]])
print(mtz)

# Estruturando NumPy arrays automaticamente
mtz = np.ones(9).reshape(3,3)
print(mtz)
# zeros
# arange
mtz = np.arange(10, 20, 2)
print(mtz)
'''

# Operações Elemento a Elemento
arr1 = np.arange(10, 20, 1)
arr2 = np.arange(30, 40, 1)

print(arr1)
print(arr2)
print(arr1+arr2)
print(np.concatenate([arr1, arr2]))

# Propriedades de um NumPy Array
# Tamanho
print(arr1.size)
# Dimensao
print(arr1.ndim)
# Formato
print(arr1.shape)
