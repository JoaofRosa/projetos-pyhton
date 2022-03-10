s = cont = 0
while True:
    n = int(input('Digiter um valor (999 pra para) '))
    if n == 999:
        break
    cont += 1
    s += n
print(f'A soma dos {cont} valores foi {s}!')
