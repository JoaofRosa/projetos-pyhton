n = 0
cont = 0
soma = 0
n = int(input('Digite um número?'))
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um número?'))
print('Vcove digitou {} numeros e a soma foi {}'. format(cont, soma))
