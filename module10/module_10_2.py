import threading
import time
from time import sleep


class Knight(threading.Thread):

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.day = 0

    def run(self):
        print(f'{self.name}, на нас напали! ')

        cnt = 100
        while True:
            if cnt <= 0:
                break
            cnt -= self.power
            if cnt < 0:
                cnt = 0
            self.day += 1

            if self.day % 10 == 0 or self.day % 10 > 4 and self.day % 10 < 10:
                print(f'{self.name}, сражается {self.day} дней ..., осталось {cnt} войнов!')
            elif self.day % 10 > 1 and self.day % 10 < 5:
                print(f'{self.name}, сражается {self.day} дня ..., осталось {cnt} войнов!')
            elif self.day % 10 == 1:
                print(f'{self.name}, сражается {self.day} день ..., осталось {cnt} войнов!')
            time.sleep(1)
        print(f'{self.name}, одержал победу спустя {self.day} дней!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print('Все битвы закончились!')
