numero = int(input("Digite um número: "))
n = 1

while (n * (n + 1) * (n + 2) ) < numero:
    n += 1

if (n * (n + 1) * (n + 2)) == numero:
    print(f"O número {numero} é triangular. ({n}, {n+1}, {n+2})")

else:
    print(f"O número {numero} não é triangular.")
