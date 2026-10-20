n = 0
soma = 0
while(n <= 500):
    if n%3 == 0 and n%2 == 1:
        soma += n
    n+=1
    print(soma)