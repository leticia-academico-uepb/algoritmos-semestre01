lado1 = float(input("Iforme o tamanho do lado 1 do triangulo: "))
lado2 = float(input("Iforme o tamanho do lado 2 do triangulo: "))
lado3 = float(input("Iforme o tamanho do lado 31 do triangulo: "))

if lado1>0 and lado2>0 and lado3>0 and lado1+lado2>lado3:

  if lado1 == lado2 and lado2 ==lado3:
    print("O triangulo é equilátero")

  elif lado1 == lado2 or lado1 == lado3 or lado2 ==lado3:
    print("O triangulo é isóceles")

  else:
    print("O triangulo é escaleno")

else:
  print("Erro! Os lados não fomam um triangulo")
