x, y, z = raw_input().split(" ")
x, y, z = int(x), int(y), int(z)

list = [x, y, z]

list_sorted = sorted(list)

for s in list_sorted:
    print (s)

print ("")

for l in list:
    print (l)
