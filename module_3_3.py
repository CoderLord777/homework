def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)

List_ = [1,2]
print_params()
print_params(List_,2)
print_params(b = 25)
print_params(c = [1,2,3])
values_list = [1,'Slovo', (5,4,3,2,5)]
values_dict = {'a':1,'b':'строка','c':True}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [1,'Slovo2']
values_list_2 = print_params(*values_list_2, 42)

