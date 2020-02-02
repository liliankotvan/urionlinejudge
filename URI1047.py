from datetime import *

entrada = raw_input().split()
Hx, Mx, Hy, My = [abs(int(x)) for x in entrada]

Dx, Dy = '1', '1'

if Hx > Hy:
    Dy = 2

if Hx == Hy:
    if Mx < My:
        Dy = 1
    else :
        Dy = 2

inicio, fim = datetime.strptime("{} {}:{}".format(Dx, Hx, Mx), "%d %H:%M"), \
              datetime.strptime("{} {}:{}".format(Dy, Hy, My), "%d %H:%M")

delta = (fim - inicio).total_seconds()

diferenca_horas = int(delta // 3600)
diferenca_minutos = int((delta % 3600) / 60)

print('O JOGO DUROU {:.0f} HORA(S) E {:.0f} MINUTO(S)'.format(diferenca_horas, diferenca_minutos))
