#Exercício em string
numero = str(input('Digite um número de 0 a 9999: '))
print(f'O seu número possui \nunidade: {numero[3]}\ndezena: {numero[2]}\ncentena: {numero[1]}\nmilhar: {numero[0]}')

#Exercício em integer
numero = int(input('Digite um número de 0 a 9999: '))
print(f'O seu número possui \nunidade: {numero % 10}\ndezena: {(numero // 10) % 10}\ncentena: {(numero // 100) % 10}\nmilhar: {(numero // 1000) % 10}')