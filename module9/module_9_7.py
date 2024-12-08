def is_prime(func):
    def wrapper(*args, **kwargs):

        number = func(*args, **kwargs)

        if number > 1:
            for i in range(2, int(number ** 0.5) + 1):
                if number % i == 0:
                    print("Составное")
                    break
            else:
                print("Простое")

        return number

    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)
