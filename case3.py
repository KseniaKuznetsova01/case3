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

while year <= years:
    year += 1
    print(year, lc.YEAR)
    print('-'*46)

