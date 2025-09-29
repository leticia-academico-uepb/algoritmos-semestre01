altura = float(input("Informe sua altura em metros: "))

if(altura>0):

  sexo = input("Informe seu sexo - M para masculino e F para Feminino: ")

  if sexo == 'M' or sexo == 'm':
    pesoIdeal = (72.7*altura) - 58

  elif sexo == 'F' or sexo == 'f':
    pesoIdeal = (62.1 * altura) - 44.7

  else:
    pesoIdeal = "Sexo inválido. Não foi possível calcular o seu ideal"

  print(pesoIdeal)

else:
   print("Erro. Confira os dados inseridos")
