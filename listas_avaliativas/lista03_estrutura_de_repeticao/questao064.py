divida = float(input("Digite o valor da dívida: R$"))
parcelas1 = 1
parcelas2 = 3
parcelas3 = 6

if divida>0:
  print("Valor da Dívida  Valor dos Juros  Quantidade de Parcelas  Valor da Parcela")
  for parcelas in range(1, 7):
     if parcelas == parcelas1:
          juros = 0
     elif parcelas == parcelas2:
         juros = divida * 0.10
     elif parcelas == parcelas3:
         juros = divida * 0.15

     valorParcela = (divida + juros) / parcelas

     print(f"R$ {divida:}           R$ {juros}                   {parcelas}                        R$ {valorParcela}")
else:
  print("O valor não é considerado um dívida")
