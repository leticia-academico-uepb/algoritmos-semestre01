repeticoes = 10

listaMedias = []; listaMediasAcima7 = []
for i in range(repeticoes):
  media = 0
  for j in range(4):
    nota = float(input(f"Digite a nota {j+1} do aluno {i+1}: "))

    while nota <0 or nota >10:
      print("Nota Inválida!")
      nota = float(input(f"Digite outra valor para nota {j+1}: "))

    media+=nota

  media/=4
  listaMedias.append(media)
  if media >= 7:
    listaMediasAcima7.append(media)

print("As médias de cada aluno:", listaMedias)
print(listaMediasAcima7)
