import time

start_time = time.time()

number = int(input())
worked_hours = int(input())
amount_per_hour = float(input())

print("NUMBER = {}".format(number))
print("SALARY = U$ {:.2f}" .format(worked_hours * amount_per_hour))

elapsed_time = time.time() - start_time
print(elapsed_time)