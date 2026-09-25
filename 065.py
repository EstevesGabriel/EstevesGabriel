num = int(input("Enter a number: "))
continuar = 's'
media = 0
maior = 0
menor = 0
termos = 0

while continuar == "s":
    termos += 1
    media += num
    if num > maior:
        maior = num
    elif menor == 0 or num < menor:
        menor = num
    continuar = str(input("Do you want to continue? (S/N): ")).lower()
    if continuar == 's':
        num = int(input("Enter a number: "))
    elif continuar == 'n':
        break

print(f'A média dos números digitados é: {media/termos} e o maior número digitado é: {maior} e o menor número digitado é: {menor}')
