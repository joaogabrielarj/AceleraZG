soma_total = 0

for numero in range(1, 1000):
  if (numero % 3 == 0) or (numero % 5 == 0):
    soma_total += numero

print(soma_total)