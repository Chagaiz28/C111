times = ['Flamengo', 'Real Madrid', 'Barcelona', 'PSG', "Al Hilal"]

print(times[0:3])

print(times[3:])

# Utilizando a função sorted, pois ao utilizar o método times.sort a posição do Barça era modificada.
ordem = sorted(times)
print(ordem)

print(times.index('Barcelona'))

