limite = 4000000

soma_dos_pares = 0

a, b = 1, 2

while a <= limite:

    if a % 2 == 0:
        soma_dos_pares += a
    
    a, b = b, a + b

print(soma_dos_pares)