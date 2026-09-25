num = int(input('Digite 999 para parar: '))
soma = 0
termos = 0


while num != 999:
    soma += num
    termos += 1
    num = int(input('Digite 999 para parar: '))

print(f'Foram digitados {termos} números e a soma entre eles é {soma}.')

