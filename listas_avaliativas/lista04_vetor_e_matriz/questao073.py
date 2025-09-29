repeticoes = 10

lista = []
for i in range (repeticoes):
  num = float(input(f"Digite o {i+1}° número: "))
  lista.append(num)

lista.reverse()
print(lista)
