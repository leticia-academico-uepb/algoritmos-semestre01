salarioOriginal = float(input("Informe o salário: "))
percentualAumento = 0

if (salarioOriginal>0):

  if(salarioOriginal<=280):
    percentualAumento = 0.20

  elif(salarioOriginal>280 and salarioOriginal<=700):
    percentualAumento = 0.15

  elif(salarioOriginal>700 and salarioOriginal<1500):
    percentualAumento = 0.10

  elif(salarioOriginal>=1500):
    percentualAumento = 0.05

  valorAumento = salarioOriginal*percentualAumento
  salarioAjustado = salarioOriginal + valorAumento

  print("Salário sem reajuste:", salarioOriginal, "R$")
  print("Percentual de aumento:", percentualAumento*100,"%")
  print("Valor do aumentno:", valorAumento, "R$")
  print("Salário com reajuste", salarioAjustado, "R$")

else:
  print("Erro! Dados inválidos.")
