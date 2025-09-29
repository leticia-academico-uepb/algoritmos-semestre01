matriz1 = []
matriz2 = []
tamanhoMatriz = 2

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
print("Menu:")
print("a) Somar as duas matrizes")
print("b) Subtrair a primeira matriz da segunda")
print("c) Adicionar uma constante às duas matrizes")
print("d) Imprimir as matrizes")

opcao = input("Escolha uma opção: ")
while opcao != "a" and opcao != "b" and opcao != "c" and opcao != "d" :
  print("Opção não encontrada. Informe novamente um a opção (a, b, c ou d)")
  opcao = input("Escolha uma opção: ")


if opcao == "a":
    print(" ")
    print("Matriz resultante da soma das matrizes 1 e 2:")
    matrizResultante = []
    for i in range(2):
      linhaDeSoma = []
      for j in range(2):
          soma = matriz1[i][j] + matriz2[i][j]
          linhaDeSoma.append(soma)
      matrizResultante.append(linhaDeSoma)
      print(matrizResultante[i])
    print(" ")
    print(matrizResultante)

else:
  if opcao == "b":
    print(" ")
    print("Matriz resultante da subtração das matrizes 1 e 2:")
    matrizResultante = []
    for i in range(2):
      linhaDeSubtracao = []
      for j in range(2):
          subtracao = matriz1[i][j] - matriz2[i][j]
          linhaDeSubtracao.append(subtracao)
      matrizResultante.append(linhaDeSubtracao)
      print(matrizResultante[i])
    print(" ")
    print(matrizResultante)

  else:
    if opcao == "c":
      constante = float(input("Digite a constante a ser somado às matrizes: "))

      print(" ")
      print(f"Matriz 1 somado a {constante}")
      for linha in matriz1:
        for i in range(len(linha)):
          linha[i]+=constante
        print(linha)

      print(" ")
      print(f"Matriz 2 somado a {constante}")
      for linha in matriz2:
        for i in range(len(linha)):
          linha[i]+=constante
        print(linha)

    else:
      if opcao == "d":
        print("Matriz 1:")
        for linha in matriz1:
            print(linha)
        print(" ")
        print("Matriz 2:")
        for linha in matriz2:
            print(linha)
