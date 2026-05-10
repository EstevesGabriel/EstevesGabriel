a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))

print('-=' * 21)
if a + b > c and b + c > a and c + a > b:
    print('Esses valores podem formar um triângulo')
    if a == b == c:
        print('Esse triângulo será  EQUILÁTERO, pois apresenta todos os lados idênticos')
    elif a == b != c or a == c != b or a != b == c:
        print('Esse triângulo será o ISÓCELES, pois apresenta apenas dois lados iguais')
    elif a != b != c != a: 
        print('Esse triângulo será ESCALENO, pois apresenta todos os lados diferentes')
else:
    print('Esses valores não podem formar um triângulo')
print('-=' * 21)