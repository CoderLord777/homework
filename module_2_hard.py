import random


def select_number1():
    number1 = random.sample(range(3, 21), 18)
    first = random.choice(number1)
    return (first)


n = select_number1()
print("Певое число ", n)
baza = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
s = []
q = ""
w = ""
for i in baza:
    for j in range(1, 21):
        if i == j:
            continue
        p = i + j
        if n % p == 0:
            q = str(i)
            w = str(j)
            if i < j:
                s.append([q + w])
            else:
                s.append([w + q])

res = []
for item in s:
    if isinstance(item, list):
        for subitem in item:
            res.append(subitem)

nres = []
for res in res:
    if res not in nres:
        nres.append(res)

password = ""
for c in nres:
    password += c
print("Пароль: ", password)
