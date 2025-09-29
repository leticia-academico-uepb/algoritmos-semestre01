numPos = float(input("Digite um valor positivo: "))
cont = 1
contPares = 0
contImpares = 0
mediaPar = 0
mediaGeral = 0

while numPos!=0 and numPos>=0:

    if numPos%2==0:
      contPares+=1
      mediaPar+=numPos
      mediaGeral+=numPos

    if numPos%2!=0:
      contImpares+=1
      mediaGeral+=numPos

    cont+=1
    numPos = float(input("Digite um valor positivo: "))

mediaGeral/=cont-1
mediaPar/=contPares

print(contPares)
print(contImpares)
print(mediaGeral)
print(mediaPar)
