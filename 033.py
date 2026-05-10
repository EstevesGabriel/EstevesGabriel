a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))
c = int(input('Digite o valor de c: '))

maiorAB = int((a + b + abs(a - b)) / 2)
maiorBC = int((maiorAB + c + abs(maiorAB - c)) / 2)
print(f'{maiorBC} é o maior dentre {a}, {b} e {c}')
