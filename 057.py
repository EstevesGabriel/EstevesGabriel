sexo = str(input('Informe seu sexo: ')).upper().strip()[0]
while sexo not in 'MmFf':
    sexo = str(input('Sexo inválido\nDigite novamente: ')).upper().strip()[0]
print(f'Sexo {sexo} validado')

