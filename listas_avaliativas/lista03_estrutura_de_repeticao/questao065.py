empregadoMaisRecenteNumero = 0
empregadoMaisRecenteMeses = float("-inf") #observação
empregadoMaisAntigoNumero = 0
empregadoMaisAntigoMeses = float("inf")

numeroEmpregado = int(input("Digite o número do empregado - digite 0  para terminar: "))

while numeroEmpregado != 0:
  mesesTrabalho = int(input("Digite o número de meses de trabalho deste empregado: "))

  if numeroEmpregado <0 or mesesTrabalho<0:
      print("Os números usados devem ser positivos")
      break

  elif mesesTrabalho > empregadoMaisRecenteMeses:
      empregadoMaisRecenteNumero = numeroEmpregado
      empregadoMaisRecenteMeses = mesesTrabalho

  elif mesesTrabalho < empregadoMaisAntigoMeses:
      empregadoMaisAntigoNumero = numeroEmpregado
      empregadoMaisAntigoMeses = mesesTrabalho

  numeroEmpregado = int(input("Digite o número do empregado - digite 0 para terminar: "))

print("O empregado mais recente é o número:", empregadoMaisRecenteNumero)
print("O empregado mais antigo é o número:", empregadoMaisAntigoNumero)
