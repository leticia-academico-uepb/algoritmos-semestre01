tamanhoMatriz = 3

matriz = []; somaDiagonalAcimaPrincipal = 0
print("Digite os elementos da matriz 3x3: ")
for i in range(tamanhoMatriz):
    linha = []
    for j in range(tamanhoMatriz):
        elemento = float(input(f"Digite o elemento [{i+1}][{j+1}]: "))
        linha.append(elemento)
        if i+1 == j:
          somaDiagonalAcimaPrincipal+=elemento
    matriz.append(linha)

print(somaDiagonalAcimaPrincipal)
