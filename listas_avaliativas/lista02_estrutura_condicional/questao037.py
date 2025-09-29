valor = int(input("Digite o valor que deseja sacar (entre 10 e 600 reais): "))

if valor >= 10 and valor <= 600:
  
  notas100 = int(valor/100);
  notas50 = int((valor%100)/50);
  notas10 = int(((valor%100)%50)/10);
  notas5 = int((((valor%100)%50)%10)/5);
  notas1 = int((((valor%100)%50)%10)%5);

  if notas100>0:
    print(notas100, "nota (s) de 100")

  if notas50>0:
    print(notas50, "nota (s) de 50")

  if notas10>0:
    print(notas10, "nota (s) de 10")

  if notas5>0:
    print(notas5, "nota (s) de 5")

  if notas1>0:
    print(notas1, "nota (s) de 1")

else:
  print("Valor inválido. O valor mínimo é de 10 reais e o máximo é de 600 reais.")
