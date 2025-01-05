import numpy as np
from random import *

data_1 = [randint(1, 20) for i in range(20)]

print("Оригинальный массив:", data_1)
print("Сумма элементов:", np.sum(data_1))
print("Среднее значение:", np.mean(data_1))
print("Квадрат каждого элемента:", np.square(data_1))
