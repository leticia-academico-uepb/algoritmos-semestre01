tamanhoMatriz =  4
matrizOriginal = []

print("Informe os valores respectivos para a matriz 4x4" )
matrizTriangular = []
for i in range(tamanhoMatriz):
    linha = []
    linhacopy = []
    for j in range(tamanhoMatriz):
        elemento = float(input(f"Digite o elemento [{i+1}][{j+1}] da matriz 1: "))
        linha.append(elemento)
        if j > i:
          linhacopy.append(0.0)
        else:
          linhacopy.append(elemento)

    matrizOriginal.append(linha)
    matrizTriangular.append(linhacopy)

print(" ")
for i in range(tamanhoMatriz):
  print(matrizOriginal[i])

print(" ")
for i in range(tamanhoMatriz):
  print(matrizTriangular[i])
  