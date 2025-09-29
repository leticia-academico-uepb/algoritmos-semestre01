listaSOs = ["Windows Server", "Unix", "Linux", "Netware", "Mac OS", "Outro"]
listaVotos = [ 0, 0, 0, 0, 0, 0 ]
cont = 0
voto = 1

while voto != 0:
  voto = int(input(f"Informe o {cont+1}° voto - de 1 a 6 e 0 para encerrar coleta: "))
  while voto <0 or voto >6:
      print("Valor Inválido. Tente Novamente")
      voto = int(input(f"Informe o {cont+1}° voto - de 1 a 6 e 0 para encerrar coleta: "))
  if voto !=0:
    cont+=1
    listaVotos[voto-1]+=1

if cont >0:
  votosVencedor = max(listaVotos)
  indiceVencedor = listaVotos.index(votosVencedor)
  soVencedor = listaSOs[indiceVencedor]

  empatados = ""
  empate = 0

  for i in range(len(listaVotos)):
    if listaVotos[i] == votosVencedor:
        empatados+=f"{listaSOs[i]}, "
        empate+=1

  print(" ")
  print(f'{"Sistema Operacional":<20} {"Votos":^20} {"%":>17}')
  print("-" * 63)

  for i in range(6):
    print(f"{listaSOs[i]:<20} {listaVotos[i]:^20} {(listaVotos[i])*100/cont:>20.2f}% ")
  print("-" * 63)
  print(f'{"Total":<20} {cont:^20}')
  print(" ")
  if empate>1:
    print(f"Houve um empate entre os sistemas {empatados}com {votosVencedor} votos cada.")
  else:
    print(f"O Sistema Operacional mais votado foi o {soVencedor}, com {votosVencedor} votos, correspondendo {(votosVencedor*100/cont):.2f}% dos votos.")

else:
  print("Programa Encerrado!")
