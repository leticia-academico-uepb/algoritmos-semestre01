nota1 = float(input("Digite a nota 1 : "))
erro = "Dados Inválidos"

if nota1>=0 and nota1<=10:

  nota2 = float(input("Digite a nota 2: "))
  if nota2>=0 and nota2<=10:

    nota3 = float(input("Digite a nota 3: "))
    if nota3>=0 and nota3<=10:

      media = (nota1+nota2+nota3)/3
      if media==10:
        print("Aprovado com Distinção")

      elif media>=7:
        print("Aprovado")

      else:
        print("Reprovado")

    else:
       print(erro)

  else:
    print(erro)

else:
  print(erro)
