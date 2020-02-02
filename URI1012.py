
a, b, c = raw_input().split(" ")

a = float(a)
b = float(b)
c = float(c)

pi = 3.14159

triangulo = a * c /2
circulo = pi * c**2
trapezio = (a + b) * c /2
quadrado = b * b
retangulo = a * b


print("TRIANGULO: {:.3f}".format(triangulo))
print("CIRCULO: {:.3f}".format(circulo))
print("TRAPEZIO: {:.3f}".format(trapezio))
print("QUADRADO: {:.3f}".format(quadrado))
print("RETANGULO: {:.3f}".format(retangulo))



'''
3.0 4.0 5.2
TRIANGULO: 7.800
CIRCULO: 84.949
TRAPEZIO: 18.200
QUADRADO: 16.000
RETANGULO: 12.000
'''