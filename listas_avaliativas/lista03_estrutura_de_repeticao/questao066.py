totalSalario = 0
totalFilhos = 0
quantidadePessoas = 0
percentualSalariosAte250 = 0
maiorSalario = 0

salario = float(input("Digite o salário (ou um valor negativo para encerrar): "))

# Processamento dos dados
while salario >= 0:

    totalSalario += salario
    quantidadePessoas += 1

    if salario <= 250:
        percentualSalariosAte250 += 1

    # Leitura do número de filhos
    numeroFilhos = int(input("Digite o número de filhos: "))
    totalFilhos += numeroFilhos

    # Verificando o maior salário
    if salario > maiorSalario:
        maiorSalario = salario

    # Próxima entrada de salário
    salario = float(input("Digite o salário (ou um valor negativo para encerrar): "))

if quantidadePessoas > 0:

    mediaSalario = totalSalario / quantidadePessoas
    mediaFilhos = totalFilhos / quantidadePessoas

    percentualSalariosAte250 = (percentualSalariosAte250 / quantidadePessoas) * 100

    print("Resultados:")
    print("Média do salário da população:", mediaSalario)
    print("Média do número de filhos:", mediaFilhos)
    print("Maior salário:", maiorSalario)
    print("Percentual de pessoas com salário até R$250,00:", percentualSalariosAte250, "%")
else:
    print("Nenhum dado foi inserido.")