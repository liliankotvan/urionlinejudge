entrada = float(raw_input())
salario = [0, 400.00, 800.00, 1200.00, 2000.00]
reajuste = [15, 12, 10, 7, 4]

if  salario[0] <= entrada <= salario[1]:
    em_percentual = reajuste[0]
    novo_salario = entrada + (entrada * em_percentual /100)
    reajuste_ganho = novo_salario - entrada
elif salario[1] < entrada <= salario[2]:
    em_percentual = reajuste[1]
    novo_salario = entrada + (entrada * em_percentual /100)
    reajuste_ganho = novo_salario - entrada
elif salario[2] < entrada <= salario[3]:
    em_percentual = reajuste[2]
    novo_salario = entrada + (entrada * em_percentual /100)
    reajuste_ganho = novo_salario - entrada
elif salario[3] < entrada <= salario[4]:
    em_percentual = reajuste[3]
    novo_salario = entrada + (entrada * em_percentual /100)
    reajuste_ganho = novo_salario - entrada
elif entrada > salario[4]:
    em_percentual = reajuste[4]
    novo_salario = entrada + (entrada * em_percentual /100)
    reajuste_ganho = novo_salario - entrada


print('Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: {:.0f} %'.format(novo_salario, reajuste_ganho, em_percentual))