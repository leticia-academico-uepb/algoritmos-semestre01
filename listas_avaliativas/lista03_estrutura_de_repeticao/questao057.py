num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
str1 = ""

if num1 < num2:
    menorNum = num1
    maiorNum = num2
else:
    menorNum = num2
    maiorNum = num1

while menorNum < maiorNum:
    str1+=f" {menorNum} "
    menorNum += 1

print("Intervalo:", str1, maiorNum)
