import math

x = float(input("Digite o valor de x: "))
arcoTan = 0
sinal = 1

for n in range(1, 51):
    termo = (sinal * (x ** (2*n - 1))) / (2*n - 1)
    arcoTan += termo
    sinal *= -1

print(f"A aproximação do arco tangente de {x} é: {arcoTan}")
