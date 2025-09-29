num = float(input("Digite um número: " ))
numMaior = num
numMenor = num

for i in range(9):
    num = float(input("Digite um número: " ))

    if num > numMaior:
        numMaior = num

    elif num < numMenor:
        numMenor = num

print("O maior número é:", numMaior)
print("O menor número é:", numMenor)
