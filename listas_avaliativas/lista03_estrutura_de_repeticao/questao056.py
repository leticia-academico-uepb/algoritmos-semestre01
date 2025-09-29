totalIdadeOtimo = 0
qtdRegular = 0
qtdBom = 0

for i in range(15):
    idade = int(input("Digite a idade do espectador {}: ".format(i + 1)))
    while idade <= 0:
            print("Idade inválida. Por favor, informe uma idade maior que 0")
            idade = int(input(f"Informe a idade do espectador {i+1}: "))

    opiniao = int(input("Digite a opinião (ótimo - 3, bom - 2, regular - 1): "))
    while opiniao != 1 or opiniao != 3 or opiniao != 3:
            print("Opnião inexistente. Por favor, informe dentro das classifcações determinadas: ")
            opinião = int(input(f"Informe a opnião válida do espectador {i+1}: "))

    if opiniao == 3:
        totalIdadeOtimo += idade
    elif opiniao == 1:
        qtdRegular += 1
    elif opiniao == 2:
        qtdBom += 1

if qtdRegular + qtdBom != 0:
    mediaIdadeOtimo = totalIdadeOtimo / (qtdRegular + qtdBom)
else:
    mediaIdadeOtimo = 0

porcentagemBom = (qtdBom / 15) * 100

print("Média das idades das pessoas que responderam ótimo:", mediaIdadeOtimo)
print("Quantidade de pessoas que responderam regular:", qtdRegular)
print("Porcentagem de pessoas que responderam bom:", porcentagemBom, "%")
