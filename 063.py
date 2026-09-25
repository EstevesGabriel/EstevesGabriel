n1 = 0
n2 = 1
fibonacci_sequence = 0

termos = int(input('Quantos termos você quer mostrar? '))

while termos != 0:
    print(fibonacci_sequence, end=' → ')
    n1 = n2
    n2 = fibonacci_sequence
    fibonacci_sequence = n1 + n2
    termos -= 1
print('Golden Ratio (φ) completed!')