time = int(input())

hour = time //3600
time %= 3600

minute = time // 60

seconds = time % 60

print("%d:%d:%d" % (hour, minute, seconds))

