cod = int(input("Digite o código do produto: "))
preco = 0
if cod > 0 and cod <= 5:
    qtd = int(input("Quantidade comprada: "))
    while cod > 0 and cod <= 5:
            if cod == 1:
                preco += 5.5 * qtd
            elif cod == 2:
                preco += 2.3 * qtd
            elif cod == 3:
                preco += 4.75 * qtd
            elif cod == 4:
                preco += 6.8  * qtd
            else:
                preco += 9.3  * qtd
            cod = int(input("Digite o código do produto: "))
            if cod == 0:
                break
            qtd = int(input("Quantidade comprada: "))

elif cod < 0 or cod > 5:
    print("Código inválido!")

print(preco)
        