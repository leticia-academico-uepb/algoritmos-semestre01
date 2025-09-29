numLitros = float(input("Quantidade de litros: "))
tipoCombustivel = input("tipo combustível - A para Alcool ou G para Gasolina: ")

limiteDescontoLitros = 20
valorLitroAlcool = 1.9
valorLitroGasolina = 2.5

if tipoCombustivel == "A" or tipoCombustivel == 'a':

    if numLitros <= limiteDescontoLitros:
        valorPago = (numLitros * valorLitroAlcool) * 0.97

    else:
        valorPago = (numLitros * valorLitroAlcool) * 0.95

else:
    if tipoCombustivel == "G" or tipoCombustivel == 'g':

        if numLitros <= limiteDescontoLitros:
            valorPago = (numLitros * valorLitroGasolina) * 0.96

        else:
            valorPago = (numLitros * valorLitroGasolina) * 0.94
    else:
        print("Informação inválida")
        valorPago = 0

print("Valor a pagar: R$", valorPago)
