quantiaAlunos = 2

gabarito = []
for i in range(10):
  respostaCorreta = input(f"Informe a resposta correta da questão {i+1}: ")
  while respostaCorreta !="a" and respostaCorreta!="b" and respostaCorreta!="c" and respostaCorreta!="d" and respostaCorreta!="e":
    print("A resposta dos Itens devem ir de A até E")
    respostaCorreta = input(f"Informe a resposta correta da questão {i+1}: ")
  gabarito.append(respostaCorreta)

matrizAlunos = []
for i in range(quantiaAlunos):
    linha = []
    contAcertos = 0
    matricula = int(input(f'Informe a matrícula do {i+1}° aluno: '))
    linha.append(matricula)
    for i in range(10):
        resposta = input(f'Resposta da questão {i+1}: ')
        linha.append(resposta)
        if resposta == gabarito[i]:
            contAcertos += 1
    linha.append(contAcertos)
    matrizAlunos.append(linha)

print("Gabarito:", gabarito)

for i in range(len(matrizAlunos)):
    print(matrizAlunos[i])

print(matrizAlunos)
