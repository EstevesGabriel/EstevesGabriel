termos = 0
soma = 0
while True:
    n = int(input("Digite um número inteiro (ou 999 para sair): "))
    if n == 999:
        break
    termos += 1
    soma += n
print(f"Quantidade de termos digitados: {termos} e a soma dos númeross foi {soma}")