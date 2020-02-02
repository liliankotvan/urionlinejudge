
code_1,units_1,price_1 = raw_input().split(" ")

code_2,units_2,price_2 = raw_input().split(" ")

code_1 = int(code_1)
units_1 = int(units_1)
price_1 = float(price_1)

code_2 = int(code_2)
units_2 = int(units_2)
price_2 = float(price_2)

valor_a_pagar = units_1*price_1 + units_2*price_2

print ("VALOR A PAGAR: R$ {:.2f}".format(valor_a_pagar))
