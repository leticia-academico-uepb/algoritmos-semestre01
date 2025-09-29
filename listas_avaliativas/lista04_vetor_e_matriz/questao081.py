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
  elemento =  input(f"Informe o {i+1}° elemento da lista 3: ")
  lista3.append(elemento)

lista4 = []
for i in range(repeticoes):
  lista4.append(lista1[i])
  lista4.append(lista2[i])
  lista4.append(lista3[i])

print("Lista intercalada: ")
print(lista4)
