num1 = float(input("Digite um número: "))
num2 = float(input("Digite um número: "))
num3 = float(input("Digite um número: "))

numMaior = num1

if(num2>numMaior):
  numMaior = num2

if(num3>numMaior):
  numMaior = num3

print("Maior número:", numMaior)
