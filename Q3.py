x = 70000
y = 180000
ano = 0
while(x < y):
    ano += 1
    x += (x * 0.035)
    y += (y * 0.015)

print(ano)
