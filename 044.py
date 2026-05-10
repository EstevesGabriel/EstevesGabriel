valor = float(input('Valor a ser pago: '))
condi_pagamento = int(input('De que forma deseja pagar pelo produto?\n' \
'[1] À vista dinheiro ou cheque (Desconto de 10%)\n' \
'[2] À vista no cartão (desconto de 5%)\n' \
'[3] Parcelado em 2x no cartão\n' \
'[4] Parcelado em 3x ou mais no cartão (Juros de 20%)\n' \
'-> '))


if condi_pagamento == 1:
    print(f'Preço final: R${valor - (valor * 0.1):.2f}')
elif condi_pagamento == 2:
    print(f'Preço final: R${valor - (valor * 0.05)}')
elif condi_pagamento == 3:
    print(f'Preço final: 2 parcelas de R${valor / 2:.2f}')
elif condi_pagamento == 4:
    parcelas = int(input('Quantidade de parcelas desejadas: '))
    print(f'Preço final: {parcelas} parcelas de R${((valor + (valor * 0.2)) / parcelas):.2f}')
else:
    condi_pagamento = 0
    print('Opção inválida de pagamento. Tente novamente.')

