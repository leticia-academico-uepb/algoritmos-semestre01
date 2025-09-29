num = int(input("Informe o valor de a ser calculado - o numero deve ser interio  entre 1 a 10: "))

if(num<1 or num>10):
  print("O numero deve ser interio ENTRE 1 a 10!")

else:
  print("Tabuado do", num)
  for i in range(10):
    print(f"{num} X {i+1} = {num*(i+1)}")
