x, y = input().split(" ")
x, y = int(x), int(y)

list = [x, y]

list_sorted = sorted(list)

if list_sorted[1] % list_sorted[0] == 0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')