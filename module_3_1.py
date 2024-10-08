calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    s = str(string)
    vozvrat = (len(s), s.upper(), s.lower())
    count_calls()
    return vozvrat


def is_contains(string, list_to_search):
    string = str(string).lower()
    list_to_search = list(list_to_search)
    count_calls()
    for item in list_to_search:
        if str(item).lower() == string:
            return True
    return False


print(string_info('Dlinna stroki s raznymi registrami'))
print(string_info('Eche odna syroka'))
print(is_contains('Lombard', ['ban', 'Lombardjinni', 'Lombard', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
