repeticoes = 10

listaNomes = []
for i in range(repeticoes):
  nome = input(f"{i+1} - Informe um nome: ")
  listaNomes.append(nome)

nomePesquisar = input("Qual nome verifcar se há dentro da lista? ")
if nomePesquisar in listaNomes:
  print(f"ACHEI")

else:
    print(f"NÃO ACHEI")
  