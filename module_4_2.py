def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    print(inner_function())
print(inner_function()) #NameError: name 'inner_function' is not defined. Did you mean: 'test_function'? не видит, т.к. "локальная" функция
print(test_function())