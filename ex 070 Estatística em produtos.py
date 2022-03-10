print('-'*20)
print('lojas joao baratão')
print('-'*20)
totM = menor = cont = 0
total = 0
barato = ' '
while True:
    produto = str(input('Nome do Produto: ')).strip().upper()
    preco = float(input('Preço: R$ '))
    cont += 1
    total += preco
    if preco > 100:
        totM += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if resp == 'N':
        break
print(f'O total gasto na compra foi R${total:.2f}')
print(f'Foram {totM} produtos que custaram mais de R$100')
print(f'O preoduto mais barato foi {barato} custa R${menor:.2f}')

