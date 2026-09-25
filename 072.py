numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    numeros_input = int(input('Digite um número de 0 a 20: '))
    if 0 <= numeros_input <= 20:
        print(f'Você digitou o número: {numeros[numeros_input]}')
        continuar = str(input('Você quer continuar? [s/n]: ')).strip().lower()
        if continuar in 'Ss':
            continue
        else:
            break            
    else:
        print('Número inválido, tente novamente')