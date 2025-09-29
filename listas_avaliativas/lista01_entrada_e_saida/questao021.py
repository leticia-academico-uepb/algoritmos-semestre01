valorHora = float(input("Informe quanto você ganha por hora: "))
horasTrabalhadas = int(input("Informe a quantidade de horas trabalhadas no mês: "))

salarioBruto = valorHora * horasTrabalhadas
somaDescontos = (11+8+5)/ 100 # IR (11%), INSS (8%), Sindicato (5%):

salarioLiquido = salarioBruto - salarioBruto*somaDescontos
print("Seu salário líquido do mês é:", salarioLiquido)
