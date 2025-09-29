numTemperaturas = int(input("Quantas temperaturas você deseja inserir? "))

if numTemperaturas <= 0:
    print("Número inválido de temperaturas.")
else:
    menorTemperatura = float('inf')
    maiorTemperatura = float('-inf')
    somaTemperatura = 0

    for i in range(numTemperaturas):
        temperatura = float(input("Digite a temperatura: "))

        somaTemperatura += temperatura
        if temperatura < menorTemperatura:
            menorTemperatura = temperatura
        if temperatura > maiorTemperatura:
            maiorTemperatura = temperatura

    mediaTemperatura = somaTemperatura / numTemperaturas

    print(f"Menor temperatura: {menorTemperatura}°C")
    print(f"Maior temperatura: {maiorTemperatura}°C")
    print(f"Média das temperaturas: {round(mediaTemperatura,2)}°C")
