n = int(input("Digite o valor de N - em quem N>0: "))
numerador = 1; denominador = 1
serie = ""
soma = 0

if(n>0):

  for i in range (n-1):

    serie+= f"{numerador}/{denominador} + "
    soma+=(numerador/denominador)
    numerador+=1; denominador+=2

  serie+=f"{numerador}/{denominador}"
  soma+=numerador/denominador

  print("S =", serie)
  print("S =", soma)

else:
  print("Use valores maiores que 0 para N")
