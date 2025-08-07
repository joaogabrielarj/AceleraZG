def maior_fator_primo(n):
    
    maior_fator = -1
    
    while n % 2 == 0:
        maior_fator = 2
        n = n / 2
        
    i = 3
    while i * i <= n:
        while n % i == 0:
            maior_fator = i
            n = n / i
        i = i + 2
        
    if n > 2:
        maior_fator = n
        
    return int(maior_fator)

numero_alvo = 600851475143
resultado = maior_fator_primo(numero_alvo)

print(f"O maior fator primo de {numero_alvo} é {resultado}")