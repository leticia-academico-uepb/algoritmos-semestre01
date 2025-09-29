matriz = []
tamanhoMatriz = 10

for i in range(1, tamanhoMatriz+1):
  linha = []
  for j in range(1, tamanhoMatriz+1):
    if i < j:
      linha.append(2*i+7*j-2)
    else:
      if i > j:
        linha.append(4*i**3 - 5*j**2 + 1)
      else:
        linha.append(3*i**2-1)

  matriz.append(linha)

print("Matriz:", matriz)
print(" ")
for i in range(tamanhoMatriz):
  print(matriz[i])
