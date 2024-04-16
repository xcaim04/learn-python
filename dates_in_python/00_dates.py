### Dates ###

# Date and time library
from datetime import datetime
from datetime import date
from datetime import time
from datetime import timedelta

def print_date(date):

    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.microsecond)
    print(date.month)
    print(date.year)
    # timestamp -> referencia unica de una fecha
    print(date.timestamp())


# Time, <class 'datetime.datetime'>
now = datetime.now()

print_date(now)
print()

# MINIMO DATOS: YEAR, MONTH, DAY
year_2023 = datetime(2023, 1, 1)

print_date(year_2023)
print()


# Encapsular tiempo, vamos a tener que rellenarlo
current_time = time(23, 1, 50)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)

# Date

current_date = date.today()
last_date = date(2022, 1, 1)

diff_date = (current_date - last_date)

print(diff_date)

# Time delta

# Nos vale para crear y operar con diferencias de fechas

init_timedelta = timedelta(200, 100, 100, weeks = 10)
finish_timedelta = timedelta(400, 100, 100, weeks=13)

print(finish_timedelta - init_timedelta)
print(current_date - finish_timedelta)