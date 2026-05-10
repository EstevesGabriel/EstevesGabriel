soma = 0
for n in range(1,7):
    num = int(input(f'Digite o {n}° valor: '))
    if num % 2 == 0:
        soma += num
    else:
        continue
print(f'A soma dos números pares foi: {soma}')