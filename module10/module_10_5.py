from multiprocessing import Pool
import datetime


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line.strip())


if __name__ == '__main__':
    list_files = [f'./file {number}.txt' for number in range(1, 5)]

    # Линейный
    start = datetime.datetime.now()
    for filename in list_files:
        read_info(filename)
    end = datetime.datetime.now()
    print(f'линейный: {end - start}')
    # линейный: 0:00: 06.925511

    # Многопроцессный
    start = datetime.datetime.now()
    with Pool() as pool:
        pool.map(read_info, list_files)
    end = datetime.datetime.now()
    print(f'многопроцессный: {end - start}')

    # многопроцессный: 0:00:02.493986
