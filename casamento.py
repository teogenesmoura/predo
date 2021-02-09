import sys
from datetime import datetime

def is_timedelta_valid(diff):
    day = get_day_from_datetime(diff)
    if(int(day) < 0):
        return False
    return True

def parse_datetime(date):
    day, time = date.split(' ')
    day = datetime(1981,12,int(day))
    day = day.strftime("%d/%m/%y")
    parsed_date = day + " " + time
    return datetime.strptime(parsed_date, '%d/%m/%y %H:%M:%S')

def get_day_from_datetime(date):
    return date.days

def mount_result(diff):
    day = diff.days
    hours, remainder = divmod(diff.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    result = str(day) + ' dia(s)\n'
    result += str(hours) + ' hora(s)\n'
    result += str(minutes) + ' minuto(s)\n'
    result += str(seconds) + ' segundo(s)'
    return result

def precifica_casamento(inicio, final):
    inicio = parse_datetime(inicio)
    final = parse_datetime(final)
    diff = final - inicio
    if(not is_timedelta_valid(diff)):
        return "Data invalida!"
    return mount_result(diff)


if __name__ == '__main__':
    print(precifica_casamento("5 08:12:23", "9 06:13:23"))
    print(precifica_casamento("1 2:2:2", "2 2:2:2"))
    print(precifica_casamento("8 08:58:14", "8 08:58:12"))
