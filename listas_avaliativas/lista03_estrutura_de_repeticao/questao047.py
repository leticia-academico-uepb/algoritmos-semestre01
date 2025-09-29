N = int(input())
fatorial = N

if N>0:

  for i in range (N-1):
    fatorial*=N-1
    print(fatorial)
    N-=1

else:
  print("Erro! Digite um valor maior que 0")
