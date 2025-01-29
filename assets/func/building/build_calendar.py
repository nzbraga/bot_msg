import calendar
import locale
import datetime

from assets.func.building.check_hour import check_hour

# Define o local como pt_BR
locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
current_month = datetime.datetime.now().month
current_day = datetime.datetime.now().day
number_month = current_month if current_month < 12 else 1
month = calendar.month_name[number_month]


def get_time():
    hour = check_hour(datetime.datetime.now().hour)
    minute = datetime.datetime.now().minute
    return (hour, minute)
