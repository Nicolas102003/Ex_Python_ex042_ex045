pes = float(input('Digite o seu peso:'))
alt = float(input('Digite a sua altura:'))
imc = pes / pow(alt,2)
if imc < 18.5:
    print('Com o IMC de {} você possui o status: ABAIXO DO PESO'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('Com o IMC de {} você possui o status: PESO IDEAL'.format(imc))
elif imc >= 25 and imc < 30:
    print('Com o IMC de {} você possui o status: SOBREPESO'.format(imc))
elif imc >=30 and imc < 40:
    print('Com o IMC de {} você passui o status: OBESIDADE'.format(imc))
elif imc >= 40:
    print('Com o IMC de {} você possui o status: OBESIDADE MORBIDA'.format(imc))
