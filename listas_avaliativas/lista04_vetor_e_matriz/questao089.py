tamanhoMatriz = 4
matriz = []

print("Digite os elementos da matriz 4x4: ")
for i in range(tamanhoMatriz):
    linha = []
    for j in range(tamanhoMatriz):
        elemento = float(input(f"Digite o elemento [{i+1}][{j+1}]: "))
        linha.append(elemento)
    matriz.append(linha)

cont = 0
for linha in matriz:
    for valor in linha:
        if valor > 10:
            cont += 1

print(f"A matriz possui {cont} valores maiores que 10.")
