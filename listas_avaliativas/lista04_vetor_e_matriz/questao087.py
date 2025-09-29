repeticoes = 20

lista = []
for i in range(repeticoes):
  num = int(input(f"Informe o {i+1}° número: "))
  lista.append(num)

lista2 = lista.copy()
lista2.remove(max(lista))

print(max(lista2))
print(lista)
