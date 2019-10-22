import local_case3 as lc
print(lc.YEARS)
years = int(input())
print(lc.START)
start = int(input())
print(lc.PROC)
proc = int(input())
print(lc.DOP)
dop = int(input())

year = 0
month = 0
osnova = start
kapital = start
suma = 0
dop1 = 0

while year < years:
    year += 1
    print(year, lc.YEAR)
    print('-' * 46)
    while month < 12:
        month += 1
        osnova = kapital + dop1
        suma = osnova * proc / 100
        kapital = osnova + suma
        dop1 = dop
        print('{:3d}\t {:.2f}\t {:.2f}\t {:.2f}'.format(month, osnova, suma, kapital ))
    if month == 12:
         month = 0
