from datetime import *

start, end = input().split(" ")
start, end = int(start*3600), int(end*3600)

Start = timedelta.seconds(start)
End = timedelta.seconds + timedelta.seconds(end)

Duracao_jogo = End - Start

print('O JOGO DUROU {} HORA(S)'.format(Duracao_jogo))