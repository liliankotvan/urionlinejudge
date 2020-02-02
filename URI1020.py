age = int(input())

years = age //365
age %= 365

months = age // 30

days = age % 30

print("{} ano(s)\n{} mes(es)\n{} dia(s)".format(years, months, days))
