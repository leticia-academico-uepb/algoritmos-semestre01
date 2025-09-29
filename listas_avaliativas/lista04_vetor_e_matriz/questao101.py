ano_2017 = [[100,200,300,400],[2700,450,600,1200],[600,400,550,450]]

ano_2018 = [[130,230,600,500],[3000,500,700,1200],[500,200,200,100]]

ano_2019 = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]

for i in range(len(ano_2017)):
    for j in range(len(ano_2017[0])):
        porcentagem = (ano_2018[i][j] - ano_2017[i][j])/ano_2017[i][j]
        ano_2019[i][j] = (1 + porcentagem) * ano_2018[i][j]

for i in range(len(ano_2019)):
    print(ano_2019[i])
    