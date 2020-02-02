x, y, z = input().split(" ")
x, y, z = float(x), float(y), float(z)

list = [x, y, z]

list_sorted = sorted(list)

if list_sorted[0] + list_sorted[1] <= list_sorted[2]:
    Area = ((x + y) * z) / 2
    print('Area = {:.1f}'.format(Area))
else:
    Perimetro = x + y + z
    print('Perimetro = {:.1f}'.format(Perimetro))