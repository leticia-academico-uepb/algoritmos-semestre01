marcas = ["A", "B", "C"]
estoque = []  # i - marcas; j - tamanhos

for i in range(len(marcas)):
    print(f"Digite as quantidades de sapatos da marca {marcas[i]}: ")
    linha = [] # quantidade por tamanho da Marca
    for j in range(6):  # 6 tamanhos de 35 a 40
        quantidade = int(input(f"Informe a quantidade do tamanho {35+j}: "))
        while quantidade < 0:
           print("Valor de quantidade inválida!")
           quantidade = int(input(f"Informe a quantidade válida do tamanho {35+j}: "))
        linha.append(quantidade)
    estoque.append(linha)

for i in range(len(estoque)):
    maioresIguais = []
    maiorQuantidade = max(estoque[i])
    for j in range(len(estoque[i])):
        if estoque[i][j] == maiorQuantidade:
            maioresIguais.append(j + 35)
    print(f"Para a marca {marcas[i]}, os tamanhos com maior quantidade em estoque são: {maioresIguais} ({maiorQuantidade} unidades).")
    