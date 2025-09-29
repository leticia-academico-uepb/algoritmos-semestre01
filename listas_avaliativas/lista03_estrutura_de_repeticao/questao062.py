N = int(input("Digite o número de termos (n): "))
r = float(input("Digite a razão (r): "))
a1 = float(input("Digite o primeiro termo (a1): "))

print("Termos da Progressão Aritmética:")
for n in range(1, N + 1):
    termo = a1 + (n - 1) * r
    print(f"a{n} = {termo}")
