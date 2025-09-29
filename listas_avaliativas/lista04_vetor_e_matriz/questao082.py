repeticoes = 30

listaIdades = []; listaAlturas = []
for i in range(repeticoes):
  idade = int(input(f"Informe a {i+1}° idade: "))
  while idade<0:
    print("Valor de idade inválido!")
    idade = int(input(f"Informe um valor válido para {i+1}° idade: "))

  altura = float(input(f"Informe a {i+1}° altura: "))
  while altura <0:
    print("Valor de altura inválido!")
    altura = float(input(f"Informe um valor válido para {i+1}° altura: "))

  listaIdades.append(idade)
  listaAlturas.append(altura)

mediaAlturas = 0
for num in listaAlturas:
    mediaAlturas += num/repeticoes

contMais13 = 0 # Contador para aluno com mais de 13 anos e altura menor que a média da turma
for i in range(len(listaIdades)):
    if listaIdades[i] > 13 and listaAlturas[i] < mediaAlturas:
        contMais13 += 1

print("Média das altura", mediaAlturas)
print(contMais13, "Aluno(s) com mais de 13 anos e altura menor que à média:")
