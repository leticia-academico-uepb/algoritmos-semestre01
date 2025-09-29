valorHora = float(input("Informe quanto você ganha por hora: "))
horasTrabalhadas = int(input("Informe a quantidade de horas trabalhadas no mês: "))

if (valorHora>0 and horasTrabalhadas>0):

    salarioBruto = valorHora * horasTrabalhadas
    valorDescontoINSS = salarioBruto*0.10

    # Laço condicional para Imposto de Renda (IR):
    valorDescontoIR = 0
    percentualDescontoIR = 0

    if(salarioBruto>900 and salarioBruto<=1500):
      percentualDescontoIR = 0.05
      valorDescontoIR = salarioBruto * percentualDescontoIR

    elif(salarioBruto>1500 and salarioBruto<=2500):
      percentualDescontoIR = 0.10
      valorDescontoIR = salarioBruto * percentualDescontoIR

    elif(salarioBruto>2500):
      percentualDescontoIR = 0.20
      valorDescontoIR = salarioBruto * percentualDescontoIR

    valorDescontoTotal = valorDescontoIR + valorDescontoINSS

    print("I. Salário bruto (", valorHora, "*", horasTrabalhadas,")           : R$", salarioBruto)
    print("II.  (-) IR (", percentualDescontoIR*100, "% )                    : R$", valorDescontoIR)
    print("III. (-) INSS ( 10% )                    : R$", valorDescontoINSS)
    print("IV. FGTS ( 11 % )                        : R$", salarioBruto*0.11)
    print("V. Total de descontos                    : R$", valorDescontoTotal)
    print("V. Salario líquido                       : R$", salarioBruto-valorDescontoTotal)

else:
  print("Erro! Dados inválidos")
