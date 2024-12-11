from datetime import datetime
from threading import Thread
from time import sleep

start = datetime.now()


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            file.write(f'Какое-то слово № {i}\n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

end = datetime.now()
time_res = end - start
print(f'Работа потоков {time_res}')

start = datetime.now()
first_thr = Thread(target=write_words, args=(10, 'example5.txt'))
second_thr = Thread(target=write_words, args=(30, 'example6.txt'))
three_thr = Thread(target=write_words, args=(200, 'example7.txt'))
four_thr = Thread(target=write_words, args=(100, 'example8.txt'))

first_thr.start()
second_thr.start()
three_thr.start()
four_thr.start()

first_thr.join()
second_thr.join()
three_thr.join()
four_thr.join()

end = datetime.now()
time_res = end - start
print(f'Работа потоков {time_res}')
