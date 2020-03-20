import datetime

while True:
    try:
        month, day = str(input()).split()

        christmas_day = datetime.datetime(year=2016, month=12, day=25)
        date_today = datetime.datetime(year=2016, month=int(month), day=int(day))

        if christmas_day == date_today:
            print('E natal!')
        elif date_today > christmas_day:
            print('Ja passou!')
        elif (christmas_day - date_today).days == 1:
            print('E vespera de natal!')
        else:
            print('Faltam {} dias para o natal!'.format(
                (christmas_day - date_today).days))
    except EOFError:
        break
