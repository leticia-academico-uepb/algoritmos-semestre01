produto1 = float(input("Informe o valor do produto 1: "))
produto2 = float(input("Informe o valor do produto 2: "))
produto3 = float(input("Informe o valor do produto 3: "))

if (produto1>0 and produto2>0 and produto3>0):

	if(produto1<produto2 and produto1<produto3):
		print("Produto 1 é mais em conta")

	elif(produto2<produto1 and produto2<produto3):
		print("Produto 2 é mais em conta")

	else:
		print("Produto 3 é mais em conta")

else:
	print("Erro! Dados Inválidos")
