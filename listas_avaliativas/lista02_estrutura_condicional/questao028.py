turno = input("Digite M - matutino ou V - Vespertino ou N - Noturno: ")

if(turno == "M" and turno == "m"):
  print("Bom Dia!")

elif(turno == "V" and turno == "v"):
  print("Boa Tarde!")

else:
    if(turno == "N" and turno == "n"):
      print("Boa Noite!")

    else:
      print("Erro! Dados inválidos.")
