while True:
    multiplica = int(input("Quer ver a tabuada de qual número?\nDigite um número negativo para sair do programa\n->  "))
    if multiplica < 0:
        break
    for c in range(1, 11):
        print(f"{multiplica} x {c} = {multiplica * c}")
    

