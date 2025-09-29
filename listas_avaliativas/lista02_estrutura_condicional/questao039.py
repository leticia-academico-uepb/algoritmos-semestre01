num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

operacao = input("Digite a operação desejada (+, -, *, /): ")
resultado = 0

if operacao == '+':
    resultado = num1 + num2
elif operacao == '-':
    resultado = num1 - num2
elif operacao == '*':
    resultado = num1 * num2
elif operacao == '/':
    if num2 != 0:
        resultado = num1 / num2
    else:
        print("Erro: divisão por zero!")
if num2!=0 and operacao != "/" : #Observação

  # Verificando par ou ímpar:
  if resultado % 2 == 0:
    parImpar = "par"
  else:
    parImpar = "ímpar"

  # Verificando positivo ou negativo:
  if resultado > 0:
    posNeg = "positivo"
  elif resultado < 0:
    posNeg = "negativo"
  else:
    posNeg = "neutro"

  # Verificando inteiro ou decimal
  if resultado % 1 == 0:
    intFloat = "inteiro"
  else:
    intFloat = "decimal"
    parImpar = "Nem par e nem ímpar, pois é decimal"

  print("O resultado da operação é:", resultado)
  print("O número é:", parImpar,",", posNeg, "e", intFloat)
