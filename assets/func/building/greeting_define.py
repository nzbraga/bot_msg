def greeting_define(hour, name):
    if hour >= 6 and hour <12:
        greeting = f'Bom dia {name},'
        return  greeting
    elif hour >= 12 and hour < 18:
        greeting = f'Boa Tarde {name},'
        return  greeting
    elif hour >= 18 and hour < 22:
        greeting = f'Boa Noite {name},'
        return  greeting


