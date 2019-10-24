import local_case3 as lc  # Caused by the localization modul.

years = int(input(lc.YEARS))  # The user enters the number of years.
start = int(input(lc.START))  # The user enters the initial capital.
proc = int(input(lc.PROC))  # The user enters the interest rate.
dop = int(input(lc.DOP))  # The user enters investment infusions.

year = 0
month = 0
osnova = start
kapital = start
suma = 0
dop1 = 0

# As long as the number of years more than the user entered is executed.
while year < years:
    year += 1
    print()
    print(year, lc.YEAR)                     # Displays the next year.
    print('-' * 45)
    print()
    print(lc.TABLE, lc.TABLE_3, lc.TABLE_4, lc.TABLE_5,
          sep='|', end='|')

    #
    while month < 12:
        month += 1
        osnova = kapital + dop1              # Fixed capital with investments.
        suma = osnova * proc / 100           # A percentage of the fixed capital.
        kapital = osnova + suma              # Capital after accrual of interest for the month.
        dop1 = dop                           # Assign the value of the investment investment variable.
        print()
        print('{:3d}\t {:.2f}\t {:.2f}\t {:.2f}'
              .format(month, osnova, suma, kapital))

    if month == 12:                          # When it comes to the last month, the program ends.
        month = 0