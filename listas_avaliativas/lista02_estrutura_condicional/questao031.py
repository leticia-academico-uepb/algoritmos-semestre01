numDia = int(input("Infrome um número correspondente ao dia (1-7): "))

if(numDia>=1 and numDia<=7):

  if(numDia == 1):
    print("Domingo")

  elif(numDia == 2):
    print("Segunda")

  elif(numDia == 3):
    print("Terça")

  elif(numDia == 4):
    print("Quarta")

  elif(numDia == 5):
    print("Quinta")

  elif(numDia == 6):
    print("Sexta")

  else:
    print("Sábado")

else:
   print("Erro! Dados inválidos.")
