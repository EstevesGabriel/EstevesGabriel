a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))

print('-=' * 21)
if a + b > c and b + c > a and c + a > b:
    print('Esses valores podem formar um triângulo')
else:
    print('Esses valores não podem formar um triângulo')
print('-=' * 21)