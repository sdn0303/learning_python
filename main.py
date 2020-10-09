# -*- Coding: UTF-8 -*-
from sort_algorithm.sort import bubble_sort, bucket_sort, selection_sort, insert_sort

if __name__ == "__main__":
    numbers_list = [9, 2, 1, 5, 7, 3, 8, 4, 6, 0]

    result = bubble_sort(numbers_list)
    print(f"result: {result}\n")

    result = selection_sort(numbers_list)
    print(f"result: {result}\n")

    result = insert_sort(numbers_list)
    print(f"result: {result}\n")

    result = bucket_sort(10)
    print(f"result: {result}\n")
