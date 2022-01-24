import datetime as dt

def friThe13th(month, year):
    # check if the 13th of this month is a Friday
    date = dt.date(year, month, 13)

    if (date.weekday() == 4):
        return True
    else:
        return False

def main():
    print(friThe13th(4, 2022))

main()
