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
    day = get_day_from_datetime(diff)
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
        print("Data invalida!")
    print(mount_result(diff))
