print('='*5,'Loja Akira','='*5)
pp = float(input('Qual o preço do produto ??'))
cp = int(input('Escolha a forma de pagamento:\n'
'[1] - À vista dinheiro cheque\n'
'[2] - À vista no cartão\n'
'[3] - Em até 2x no cartão\n'
'[4] - 3x ou mais normal no cartão\n'
'Sua opção:'))
if cp == 1:
    d = (10 * pp) / 100
    vf = pp - d
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(pp,vf))
elif cp == 2:
    d = (5 * pp) / 100
    vf = pp - d
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(pp,vf))
elif cp == 3:
    print('Sua compra vai ser parcelada em 2x de R${:.2f}\nSua compra vai custar R${:.2f}'.format((pp/2),pp))
elif cp == 4:
    desc = int(input('Em quantas vezes você pode parcelar ??'))
    total = pp + (pp * 20 / 100)
    parcela = total / desc
    print('Sua compra vai ser parcelada em {}x de R${:.2f} COM JUROS\n Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(desc,parcela,pp,total))


