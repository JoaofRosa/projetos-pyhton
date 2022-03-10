from random import randint
v = 0
while True:
    jogador = int(input('Digite um valor'))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou impar?[P/I]')).strip().upper()[0]
    print(f'voce jogou {jogador} e o computador {computador}. total de {total}')
    print('deu par' if total % 2 == 0 else 'deu impat')
    if tipo == 'P':
        if total % 2 == 0:
            print('Voce venceu')
            v += 1
        else:
            print('voce perdeu')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('voce venceu')
            v += 1
        else:
            print('voce perdeu')
            break
        print('vamos joga novamente')
print(f' game over , voce venceu {v} vezes')
