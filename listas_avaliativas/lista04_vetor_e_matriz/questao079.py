repeticoes = 3

listaA = []; somaQuadrados = 0
for i in range(repeticoes):
  num = int(input(f"Informe o {i+1}° número inteiro: "))
  listaA.append(num)

for i in range(repeticoes):
  somaQuadrados+=(listaA[i])**2

print("Soma:", somaQuadrados)
