N = int(input("Informe um valor máximo para o denominador: "))

numerador = 1; denominador = 1
H = 0

if N>0:

  for i in range (N):

    H+=(numerador/denominador)
    print(numerador, "/", denominador, "; Soma:", round(H,3) )
    denominador+=1

else:
  print("Erro! Dados não compátiveis. Informe um valor maior que 0.")
