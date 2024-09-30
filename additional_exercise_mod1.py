grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students2=sorted(list(students))
result={}
for i in range(len(students2)):
    result[students2[i]]=float(sum(grades[i])/len(grades[i]))
print(result)