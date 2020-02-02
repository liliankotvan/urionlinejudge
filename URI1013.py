a, b, c = raw_input().split(" ")

a = int(a)
b = int(b)
c = int(c)

maior_ab = (a + b + abs(a - b))/2

maior_final = (maior_ab + c + abs(maior_ab - c))/2

print ("{} eh o maior".format(maior_final))

