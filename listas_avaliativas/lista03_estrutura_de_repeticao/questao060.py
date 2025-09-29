n = int(input("Digite a quantidade de pessoas na turma: "))
idades = 0

if n>0:
  for i in range(n):
      idade = int(input(f"Digite a idade da pessoa {i+1}: "))
      while idade <= 0:
              print("Idade inválida. Por favor, informe uma idade maior que 0")
              idade = int(input(f"Informe a idade do espectador {i+1}: "))
      idades+=idade

  mediaIdades = (idades) / n
  mediaIdades = int(mediaIdades)

  if 0 <= mediaIdades <= 25:
    print("A média de idade da turma é",mediaIdades, "logo a turma é jovem.")
  elif 26 <= mediaIdades <= 60:
    print("A média de idade da turma é",mediaIdades, "logo a turma é adulta.")
  else:
    print("A média de idade da turma é",mediaIdades, "logo a turma é idosa.")

else:
  print("numero de pessoas deve ser maior que 0")
