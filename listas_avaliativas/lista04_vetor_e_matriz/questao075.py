repeticoes = 20

listaInteiros = []; listaPares = []; listaImpares = []
for i in range(repeticoes):
  num = int(input(f"Digite o {i+1}° número: "))
  listaInteiros.append(num)
  if num %2 == 0:
    listaPares.append(num)
  else:
    listaImpares.append(num)

print("Inteiros :", listaInteiros)
print("Pares :", listaPares)
print("Impares :", listaImpares)
