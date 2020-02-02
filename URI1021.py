N = float(input())

print("NOTAS:")

banknotes = [100, 50, 20, 10, 5, 2]

for b in banknotes:
    numero_notas = int(N / b)
    N = round(N % b, 2)

    print("{} nota(s) de R$ {:.2f}".format(numero_notas, b))

print("MOEDAS:")

coins = [1.00, 0.50, 0.25, 0.10, 0.05, 0.01]

for c in coins:
    numero_moedas = int(N / c)
    N = round(N % c, 2)

    print("{} moeda(s) de R$ {:.2f}".format(numero_moedas, c))