tamanhoMatriz = 5

matriz = []
print("Digite os elementos da matriz 5x5: ")
for i in range(tamanhoMatriz):
    linha = []
    for j in range(tamanhoMatriz):
        elemento = float(input(f"Digite o elemento [{i+1}][{j+1}]: "))
        linha.append(elemento)
    matriz.append(linha)

for i in range(tamanhoMatriz):
  print(matriz[i])

print(" ")
valorBuscado = int(input("Informe um valor para ser buscado dentro da matriz: "))
cont = 0

for i in range(tamanhoMatriz):
  for j in range(tamanhoMatriz):
    if matriz[i][j] == valorBuscado:
      print(f"O valor {valorBuscado} foi encontrado na linha {i+1} coluna {j+1}")
      cont+=1

if cont>0:
  print(f"Foram encontrados {cont} correspondêcias na matriz.")
else:
  print(valorBuscado, "não foi encontrado.")
