N = int(input("Difite o valor do tamanho da sequencia: "))
termoA = int(input("Informe o primeiro valor da sequencia: "))
termoB = int(input("Informe o segundo valor da sequencia: "))

fetuccine = f"{termoA} {termoB} "

if N>=3:
  for i in range(1, N-1, +1):

    if i%2 == 0:
      termoI = termoB+termoA

    else:
      termoI = termoB-termoA

    fetuccine+=f"{termoI} "
    termoA = termoB
    termoB = termoI

else:
  print("A sequência deve ser apresentada com ao menos 3 termos")

print("A sequência ficou dessa forma:", fetuccine)
