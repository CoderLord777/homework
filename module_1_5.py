immutable_var = (43,"Тополь",15.5,False)
print(immutable_var)
immutable_var[0]=42 #Элемент кортежа нельзя изменить потому что кортеж содержит в себе неизменяемы объекты
mutable_list = ["Very","Good","well"]
for i in range(len(mutable_list)):
    mutable_list[i]=input("Введите новый элемент списка ") #Захотелось изменить все элементы списка вводом, а не по строчно через индексы, извините)
print(mutable_list)

