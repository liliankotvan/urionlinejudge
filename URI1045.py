x, y, z = input().split(" ")
x, y, z = float(x), float(y), float(z)

list = [x, y, z]
list_sorted = sorted(list)

if list_sorted[2] >= list_sorted[0] + list_sorted[1]:
    print('NAO FORMA TRIANGULO')
else:
    if list_sorted[2]**2 == (list_sorted[0]**2 + list_sorted[1]**2):
        print('TRIANGULO RETANGULO')
    elif list_sorted[2]**2 > (list_sorted[0]**2 + list_sorted[1]**2):
        print('TRIANGULO OBTUSANGULO')
    else:
        print('TRIANGULO ACUTANGULO')

    if list_sorted[2] == list_sorted[0] == list_sorted[1]:
        print('TRIANGULO EQUILATERO')
    elif list_sorted[0] == list_sorted[1] or list_sorted[0] == list_sorted[2] or list_sorted[1] == list_sorted[2]:
        print('TRIANGULO ISOSCELES')
        