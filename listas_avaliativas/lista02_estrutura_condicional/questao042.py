kilosMorango = float(input("Kg (s) de Morango comprados: "))
kilosMaca = float(input("Kg (s) de Maçã comprados: "))

if (kilosMorango>=0 and kilosMaca>=0):
  valorTotalMorango = kilosMorango * 2.50
  valorTotalMaca = kilosMaca * 1.80

  kilosFrutas = kilosMorango + kilosMaca

  if(kilosMorango>5):
    valorTotalMorango = round((kilosMorango * 2.20), 2) #Observação ex: kilos = 6

  if(kilosMaca>5):
     valorTotalMaca = kilosMaca * 1.50

  valorTotalFrutas = valorTotalMorango + valorTotalMaca #Observção

  if(kilosFrutas>8 or valorTotalFrutas>25):
    valorTotalFrutas-=valorTotalFrutas*(10/100)

  print("Valor a ser pago: ", valorTotalFrutas)
  # print(valorTotalMorango)
  # print(valorTotalMaca)

else:
  print("Erro! Dados inválidos")
