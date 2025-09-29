listaNotas = []
nota = float(input("Digite a 1° nota - nota de 0 a 10 e -1 para encerrar: "))
cont = 0

if nota ==-1:
  print("Programa Encerrado")

else:
  while nota != -1:
     if nota>0 and nota <= 10:
        listaNotas.append(nota)
        cont+=1
     else:
        print("Nota inválida. Insira uma nota entre 0 e 10.")

     nota = float(input(f"Digite a {cont+1}° nota - nota de 0 a 10 e -1 para encerrar: "))

  quantidade = len(listaNotas)
  listaInversa = listaNotas[::-1]

  soma = 0
  for valor in listaNotas:
    soma += valor
  media = soma / quantidade

  acimaMedia = 0
  abaixoSete = 0
  for valor in listaNotas:
      if valor > media:
        acimaMedia += 1
      if valor < 7:
       abaixoSete+=1

  print("Quantidade de valores lidos:", quantidade)
  print("Valores informados:", listaNotas)
  print("Valores informados na ordem inversa:", listaInversa)
  print("Soma dos valores:", soma)
  print("Média dos valores:", media)
  print("Quantidade de valores acima da média:", acimaMedia)
  print("Quantidade de valores abaixo de sete:", abaixoSete)
  print("Programa encerrado.")
