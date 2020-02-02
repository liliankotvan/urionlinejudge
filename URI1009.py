import time

start_time = time.time()

name = raw_input()
fixed_salary = float(input())
total_value_sold = float(input())

total_salary = fixed_salary + total_value_sold * 0.15

print("TOTAL = R$ {:.2f}" .format(total_salary))

elapsed_time = time.time() - start_time
print (elapsed_time)
