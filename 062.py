pa = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
limitador = 10
continuar = 0
termos = 0

while True:
    limitador += continuar
    while limitador != 0:
        print(pa, end=' → ')
        pa += razao
        termos += 1
        limitador -= 1
    print('PAUSA')
    continuar = int(input('Quantos termos você quer mostrar a mais? '))
    if continuar == 0:
        print(f'Fim da PA\nForam mostrados {termos} termos no total.')
        break


