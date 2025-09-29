nota1 = float(input("Informe a nota 1: "))
nota2 = float(input("Informe a nota 2: "))

if nota1>=0 and nota1<=10 and nota2>=0 and nota2<=10:

  media = (nota1+nota2)/2

  #definir conceito

  if media <=10 and media >=9:
    nota = "A"

  elif media <9 and media >=7.5:
    nota = "B"

  elif media <7.5 and media >=6:
    nota = "C"

  elif media <6 and media >=4:
    nota = "D"

  else:
    nota = "E"

  #Verificar conceito
  if nota == "A" or nota == "B" or nota == "C":
    print("APROVADO")

  else:
    print("REPROVADO")

else:
  print("Erro! Dados Inválidos")
