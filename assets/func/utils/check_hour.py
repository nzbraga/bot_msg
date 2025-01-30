def check_hour(hour):
    if hour >= 22 or hour < 6:
        new_hour =6
        return new_hour
    else:
        return hour