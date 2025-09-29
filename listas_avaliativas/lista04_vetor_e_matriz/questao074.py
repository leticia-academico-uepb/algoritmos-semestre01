repeticoes = 40

listaNotas = []; media = 0
for i in range(repeticoes):
  nota = float(input(f"Digite a nota {i+1}: "))
  while nota <0 or nota >10:
    print("Nota Inválida!")
    nota = float(input(f"Digite outra valor para nota {i+1}: "))
  listaNotas.append(nota)
  media+=nota/repeticoes

print(f"As notas são: {listaNotas} e a média delas é {media}")
