def change_owed(value):
    if isnumber(value):
        coins_counter = get_coins(value)
        return coins_counter
    else:
        return 'Invalid value'


def get_coins(change):
    coins = 0
    while change != 0:
        if change >= 25:
            change = change - 25
        elif change >= 10:
            change = change - 10
        elif change >= 5:
            change = change - 5
        elif change >= 1:
            change = change - 1
        coins += 1
    return coins


def get_value(msg):
    while True:
        try:
            value = int(input(msg))
            if value > 0:
                return value
        except(ValueError, TypeError):
            print('\033[0;31mThe value must to be a number\033[m')
        except KeyboardInterrupt:
            print('\n\033[0;31mInterrupted by user\033[m')
            return 0


def isnumber(mynumber):
    return str(mynumber).isdigit()
