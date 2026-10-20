dividendo = int(input())
divisor = int(input()) 
quociente = 0
resto = 0

if divisor != 0:
    while(dividendo >= divisor):
        dividendo -= divisor
        quociente += 1
    resto = dividendo

print(quociente, resto)
