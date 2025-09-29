nQuad = int(input("informe a quantidade de quadriláteros a ser calculado"))

for i in range (nQuad):
  lado = float(input("Digite um valor para o lado do quadrilátero: "))
  if lado>0:
    area = lado*lado
    print("Area do quadrilátero", i+1, "=",area, "u.m.")
  else:
    print("Erro! a unidade de medida não pode ser negativa")
