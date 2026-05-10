frase = str(input('Digite uma frase: ')).upper()
print(f'Sua frase possui: {frase.count('A')} A')
print(f'O primeiro A da sua frase está na posição {frase.find('A', 0, -1)}')
print(f'O último A da sua frase está na posição {frase.rfind('A')}')

