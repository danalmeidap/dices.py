from operations import get_value, change_owed

value = get_value("Change owed: ")
coins = change_owed(value)
print(coins)
