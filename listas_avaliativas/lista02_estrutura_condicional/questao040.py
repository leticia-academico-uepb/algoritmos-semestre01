sim = 0

resposta = input("Telefonou para a vítima? - responda com sim ou não. resp: ")
if resposta == 'sim' or resposta == 'Sim':
    sim += 1

resposta = input("Esteve no local do crime? - responda com sim ou não. resp: ")
if resposta == 'sim' or resposta == 'Sim':
    sim += 1

resposta = input("Mora perto da vítima? - responda com sim ou não. resp: ")
if resposta == 'sim' or resposta == 'Sim':
    sim += 1

resposta = input("Devia para a vítima? - responda com sim ou não. resp: ")
if resposta == 'sim' or resposta == 'Sim':
    sim += 1

resposta = input("Já trabalhou com a vítima? - responda com sim ou não. resp: ")
if resposta == 'sim' or resposta == 'Sim':
    sim += 1

if sim == 2:
    print("Status: suspeito.")

elif 3 <= sim <= 4:
    print("Status: cúmplice.")

elif sim == 5:
    print("Status: assassino.")
    
else:
    print("Status: inocente.")
