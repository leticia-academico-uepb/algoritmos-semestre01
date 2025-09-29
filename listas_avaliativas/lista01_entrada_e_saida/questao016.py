nomeVendedor = (input("Nome: "))
salarioFixo = float(input("Salário: "))
valorVendasEfetuadas = int(input("Vendas: "))

taxaComissao = 15/100
salarioFinal = salarioFixo + valorVendasEfetuadas*taxaComissao

print("Vendedor:", nomeVendedor)
print("Salário Fixo:", salarioFixo)
print("Salario com comissão:", salarioFinal)
