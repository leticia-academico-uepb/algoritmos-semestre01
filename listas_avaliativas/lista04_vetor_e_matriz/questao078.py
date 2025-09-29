repeticoes = 10

listaIdade = []; listaAltura = []
for i in range(repeticoes):
  idade = int(input(f"Informe a {i+1}° idade: "))
  while idade<0:
    print("Valor de idade inválido!")
    idade = int(input(f"Informe um valor válido para {i+1}° idade: "))

  altura = float(input(f"Informe a {i+1}° altura: "))
  while altura <0:
    print("Valor de altura inválido!")
    altura = float(input(f"Informe um valor válido para {i+1}° altura: "))

  listaIdade.append(idade)
  listaAltura.append(altura)

maiorAltura = max(listaAltura)
indiceMaiorAltura = listaAltura.index(maiorAltura)

idadeMaiorAltura = listaIdade[indiceMaiorAltura]
print(f"A pesoa mais alta, com {maiorAltura} m de altura, tem {idadeMaiorAltura} anos.")
