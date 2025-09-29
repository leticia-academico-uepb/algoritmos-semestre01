valorDepositado = float(input("Valor Depositado: "))

juroFixo = 0.7/100

rendimentoMes = valorDepositado + valorDepositado * juroFixo
print("rendimento mensal:", rendimentoMes)
