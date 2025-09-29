print("informe o resultado do 1° jogo")
num1 = int(input("total de gols que o time fez: "))
num2 = int(input("total de gols que o time adversário fez: "))
pontos = 0
cont=1

while num1 >=0 and num2 >=0:

  if num1 > num2:
    pontos+=3
  elif(num1 == num2):
    pontos+=1

  print(f"informe o resultado do {cont+1}° jogo")
  num1 = int(input("total de gols que o time fez: "))
  num2 = int(input("total de gols que o time adversário fez: "))
  cont+=1

print("Pontos:", pontos)
