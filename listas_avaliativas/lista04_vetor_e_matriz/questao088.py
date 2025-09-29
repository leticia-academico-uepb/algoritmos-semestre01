num  = int(input("Informe o número: "))
numBinario =[]

if num > 127 or num < -127:
    print("Não é possível representar")

else:
    # Analisa o sinal
    if num < 0 :
        sinal = 1
        num = num * (-1) # Converte o número para um valor positivo - facilitar condição do while

    else:
        sinal = 0

    # Calcula a magnitude
    while num > 0:
            resto = num % 2
            numBinario.append(resto)
            num = num // 2

    # Completa com zero, se necessário. Deve ter um total de 7 bits (magnitude)
    for i in range(7-len(numBinario)):
        numBinario.append(0)

    numBinario.append(sinal) # adiciona o sinal

    #Inverte o número
    numBinario.reverse()
    print(numBinario)
