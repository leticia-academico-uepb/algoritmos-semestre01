tamanhoArquivo = float(input("Informe o tamanho do arquivo em MB: "))
velocidadeInternet = float(input("Informe a velocidade da internet em MBps: "))

tempoDownload = tamanhoArquivo/velocidadeInternet
print("Tempo de Download em segundos:", tempoDownload)
