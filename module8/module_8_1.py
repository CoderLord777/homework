def add_everything_up(a, b):
    try:
        res = a + b
        if isinstance(res, (int, float)):
            return round(res, 3)
    except TypeError as exc:
        if isinstance(a, str):
            return a + str(b)
        else:
            return str(a) + str(b)


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
