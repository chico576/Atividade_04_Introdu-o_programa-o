n = int(input("Digite um número: "))
distancia = n
passo = 0
passof = 0
max = 0
inicial = 0
while n < 1:
    print("Valor inválido!")
    n = int(input())

while distancia >= 1:
    while n > 1:
        if n%2 == 0:
            n /= 2
            passo += 1
            if max < n:
                max = n
        else:
            n = (n * 3) + 1
            passo += 1
            if max < n:
                max = n

    if passof < passo:
        passof = passo
        passo = 0
        inicial = distancia
    else:
        passo = 0

    distancia -= 1
    n = distancia

print(f"{inicial} é o valor inicial")
print(f"{passof} passos")
print(f"{max:.0f} é o valor máximo")

    
        