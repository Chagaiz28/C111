import numpy as np

np.random.seed(5)

arrp = np.random.rand(5)
arrn = np.random.rand(5)

arr = np.concatenate((arrp, arrn))
arr = 100 * arr

arr_int = arr.astype(int)  # Convertendo para inteiros

print("Array original:")
print(arr)

print("\nArray com partes inteiras:")
print(arr_int)
