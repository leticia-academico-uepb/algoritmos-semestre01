for i in range(1, 31):
    somaNotas = 0
    for j in range(1,3):
        nota = float(input(f"Informe a nota {j} do aluno {i}: "))
        while nota < 0 or nota > 10:
            print("Nota inválida. Por favor, informe uma nota entre 0 e 10.")
            nota = float(input(f"Informe a nota {j} do aluno {i}: "))
        somaNotas += nota

    media = somaNotas / 2

    # Verificar situação do aluno
    if media < 0 or media > 10:
        situacao = "Nota inválida"
    elif media < 5:
        situacao = "Reprovado"
    elif media < 7:
        situacao = "Recuperação"
    else:
        situacao = "Aprovado"

    print(f"A média do aluno {i}: {media}")
    print(f"Situação do aluno {i}: {situacao}")
