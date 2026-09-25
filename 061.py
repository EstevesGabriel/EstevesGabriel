#Variáveis da PA
pa = int(input('Digite o primeiro termo de uma PA: '))
razao = int(input('Digite a razão da PA: '))
limitador = 0

while limitador != 10:
    print(pa, end=' -> ')
    pa += razao
    limitador += 1
print('Fim da PA')