listaMeses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro'
, 'Outubro', 'Novembro', 'Dezembro']
listaTemperaturas = []

mediaAnual = 0
for i in range(12):
  temperatura = float(input(f"Informe a temperatura média de {listaMeses[i]}: "))
  listaTemperaturas.append(temperatura)
  mediaAnual+=temperatura/12

for i in range(12):
  if listaTemperaturas[i] > mediaAnual:
    print(f"{listaMeses[i]}: {listaTemperaturas[i]}")
