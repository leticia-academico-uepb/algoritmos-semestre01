tamanhoMatriz = 5

matrizIdentidade = []
for i in range(tamanhoMatriz):
  linha = []
  for j in range(tamanhoMatriz):
    if j == i:
      linha.append(1)
    else:
      linha.append(0)

  matrizIdentidade.append(linha)

print(matrizIdentidade)
print(" ")

for i in range(tamanhoMatriz):
  print(matrizIdentidade[i])
