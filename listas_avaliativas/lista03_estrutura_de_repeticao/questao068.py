print("                Cardápio                  ")
print("")
print("ESPECIFICAÇÃO	       CÓDIGO 	    	PREÇO")
print("Cachorro Quente        100         R$ 1,20")
print("Bauru Simples          101        	R$ 1,30")
print("Bauru com ovo          102       	R$ 1,50")
print("Hambúrguer             103       	R$ 1,20")
print("Cheeseburguer          104        	R$ 1,30")
print("Refrigerante           105       	R$ 1,00")
print("")

iniciar = input("Deseja comprar algo? S - Sim ou N - Não ")
continuar = "C" # C - continuar e F - Finalizar
valorCadaPedido = 0
valorTotalPedidos = 0

if iniciar == "S" or iniciar == "s":
    print("Para finalizar a compra a qualquer momento é só digitar F - finalizar")

    while continuar == "C" or continuar == "c":

      codProduto = input("Informe o codigo do produto: ")

      if codProduto == "F" or codProduto == "f":
        break

      elif codProduto !="F" and codProduto !="F" and int(codProduto) <100 or int(codProduto)>105:

        print("Código inválido")
        continuar = input("Deseja continuar? C - Continuar ou F - finalizar:")

      else:

        quantProduto = input("Informe a quantidade desse produto a ser comprado: ")

        if (quantProduto == "F" or quantProduto == "f"):
          break

        elif int(quantProduto)<0:
          print("Valor inválido")
          continuar = input("Deseja continuar? C - Continuar ou F - finalizar:")

        elif codProduto == "100" or codProduto == "103": # Cahorro Quente, Hamburguer
         valorCadaPedido = int(quantProduto)*1.20

        elif codProduto == "101" or codProduto == "104":
         valorCadaPedido = int(quantProduto)*1.30

        elif codProduto == "102":
         valorCadaPedido = int(quantProduto)*1.50

        else: #Refrigerante
         valorCadaPedido = int(quantProduto)*1

      valorTotalPedidos+=valorCadaPedido
      print(f"valor a pagar pelos itens: R$", valorCadaPedido)

    print("Valor total a pagar: R$", valorTotalPedidos)

else:
  print("Tudo bem! Esperamos que um dia sejas nosso (a) clinte :)")
