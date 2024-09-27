my_dict = {'Sima':1955,'Rita': 1965,'Lida': 1999}
print(my_dict)
print(my_dict.get('Rita'),my_dict.get('Lena',"Такого имени нет в словаре"))
my_dict.update({'Lena':2000,
                'kira':1998})
print(my_dict)
a=my_dict.pop('Lida')
print(a)
print(my_dict)
my_set={5,5,'copy','copy',3.14,3.14,(1,1,2,2),(1,1,2,2)}
print(my_set)
my_set.add(77)
my_set.add('road')
print(my_set)
my_set.remove(3.14)
print(my_set)

