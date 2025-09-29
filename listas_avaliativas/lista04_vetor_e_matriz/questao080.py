repeticoes = 10

lista1 = []
for i in range(repeticoes):
  elemento =  input(f"Informe o {i+1}° elemento da lista 1: ")
  lista1.append(elemento)

lista2 = []
for i in range(repeticoes):
  elemento =  input(f"Informe o {i+1}° elemento da lista 2: ")
  lista2.append(elemento)

lista3 = []
for i in range(repeticoes):
  lista3.append(lista1[i])
  lista3.append(lista2[i])

print("Lista intercalada: ")
print(lista3)
