while True:
    saque = int(input('Qual o valor deseja sacar?'))
    if saque > 1:
        break

    maxcedulas = int(input('Valor máximo das cédulas (1 - 2 - 5 - 10 - 20 - 50 - 100)'))
while maxcedulas not in [1, 2, 5, 10, 20, 50, 100] or maxcedulas < saque:
       maxcedulas = int(input('Valor informado inválido. Digite o valor máximo de cédula desejado:'))

       




