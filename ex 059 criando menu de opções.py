from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('=='*10)
    print('1: somar\n1: multiplicar\n3: maior\n4: novos números\n5: sair do programa')
    print('=='*10)
    opcao = int(input('Qual é sua opção?'))
    if opcao == 1:
        soma = n1 + n2
        print('A soma de {} + {} = {}'.format(n1, n2, soma))
    elif opcao == 2:
        mult = n1 * n2
        print('A multiplicação de {} x {} = {}'.format(n1, n2, mult))
    elif opcao == 3:
       if n1 > n2:
           maior = n1
       else:
           maior = n2
           print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
    elif opcao == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Filanizando...')
    else:
        print('Opção inválida. Tente novamente')
    sleep(1)
print('Fim do programa! Volte sempre!')