tamanhoMatriz = 4

matriz1 = []; matriz2 = []
print("Informe os valores respectivos para a PRIMEIRA matriz" )
for i in range(tamanhoMatriz):
    linha = []
    for j in range(tamanhoMatriz):
        elemento = float(input(f"Digite o elemento [{i+1}][{j+1}] da matriz 1: "))
        linha.append(elemento)
    matriz1.append(linha)

print("Informe os valores respectivos para a SEGUNDA matriz" )
for i in range(tamanhoMatriz):
    linha = []
    for j in range(tamanhoMatriz):
        elemento = float(input(f"Digite o elemento [{i+1}][{j+1}] da matriz 2: "))
        linha.append(elemento)
    matriz2.append(linha)

print(" ")
matrizMaiorDaPosicao = []
for i in range(tamanhoMatriz):
  linha = []
  for j in range(tamanhoMatriz):
    maiorEntre1e2 = max(matriz1[i][j], matriz2[i][j])
    linha.append(maiorEntre1e2)

  matrizMaiorDaPosicao.append(linha)

print("Matriz com os maiores valores de cada posição:", matrizMaiorDaPosicao)
print(" ")
for i in range(tamanhoMatriz):
  print(matrizMaiorDaPosicao[i])
