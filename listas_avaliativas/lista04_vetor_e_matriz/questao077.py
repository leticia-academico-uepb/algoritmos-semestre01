repeticoes = 50

soma = 0
multiplicacao = 1
listaNum = []

for i in range(repeticoes):
  num = int(input(f"informe o {i+1}° número: "))
  soma+=num
  multiplicacao*=num
  listaNum.append(num)

print("Soma:", soma)
print("Multiplicação:", multiplicacao)
print("Lista dos números:", listaNum)
