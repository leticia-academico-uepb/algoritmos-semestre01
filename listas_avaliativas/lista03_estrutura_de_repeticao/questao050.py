base = int(input("Informe o valor da Base: "))
expoente = int(input("Informe o valor do expoente: "))
potencia = 1

for i in range(expoente):
  potencia *= base

print(base, "^", expoente, "é", potencia)
