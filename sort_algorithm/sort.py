# -*- Coding: UTF-8 -*-
import time
import random


def time_measure(func):
    def __decorator(*args, **kwargs):
        start = time.time()
        print('Measure execution time.')
        print('func: {}'.format(func.__name__))
        f = func(*args, **kwargs)
        end = time.time() - start
        m, s = divmod(end, 60)
        print('Elapsed time:{0} [sec], {1} [min]'.format(s, m))
        return f

    return __decorator


@time_measure
def bubble_sort(numbers):
    for idx in reversed(range(len(numbers))):
        for i in range(idx):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
    return numbers


@time_measure
def selection_sort(numbers):
    for idx in range(len(numbers)):
        mini = idx
        for i in range(idx + 1, len(numbers)):
            if numbers[mini] > numbers[i]:
                mini = i
        tmp = numbers[mini]
        numbers[mini] = numbers[idx]
        numbers[idx] = tmp
    return numbers


@time_measure
def insert_sort(numbers):
    for idx in range(len(numbers)):
        for i in reversed(range(idx)):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
            else:
                break

    return numbers


@time_measure
def bucket_sort(max_num):
    numbers = [random.randint(1, 10) for _ in range(15)]
    list_counter = [0] * (max_num + 1)
    for i in numbers:
        list_counter[i] += 1
    cnt = 0
    for n in range(len(list_counter)):
        for i in range(list_counter[n]):
            numbers[i] = n
            cnt += 1
    return numbers
