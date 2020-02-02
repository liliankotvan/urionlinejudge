import math

a, b, c = raw_input().split(" ")
a, b, c = float(a), float(b), float(c)

if a == 0 or ((b**2) - (4*a*c)) < 0:

    print ("Impossivel calcular")

else:
    bhaskara_positivo = (-b + math.sqrt((b**2) - (4*a*c)))/ (2*a)

    bhaskara_negativo = (-b - math.sqrt((b**2) - (4*a*c)))/ (2*a)

    print ("R1 = {:.5f}".format(bhaskara_positivo))
    print ("R2 = {:.5f}".format(bhaskara_negativo))
