distance = int(input('Digite a distância em Km da sua viagem: '))

if distance <= 200:
    print(f'Sua viagem custará R${float(distance * 0.50)}')
elif distance > 200:
    print(f'Sua viagem teve uma promoção, ele custará R${distance * 0.45}')