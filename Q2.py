n = int(input())
menor = n
maior = 0
soma = 0
while(n != -1):
    soma += n
    if n > maior:
        maior = n

    elif n < menor:
        menor = n
    n = int(input())

print(menor, maior, soma)