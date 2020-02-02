valor = int(input())

notas = [100, 50, 20, 10, 5, 2, 1]

print(valor)

for n in range(len(notas)):
    divisao = valor / notas[n]

    inteiro = divisao - (divisao % 1)

    print("{} nota(s) de R$ {},00".format(inteiro, notas[n]))

    valor = valor % notas[n]