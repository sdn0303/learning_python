# -*- Coding: UTF-8 -*-


def bubble_sort(numbers):
    for idx in reversed(range(len(numbers))):
        for i in range(idx):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
    return numbers


def selection_sort(numbers):
    for idx in range(len(numbers)):
        mini = idx
        for i in range(idx+1, len(numbers)):
            if numbers[mini] > numbers[i]:
                mini = i
        tmp = numbers[mini]
        numbers[mini] = numbers[idx]
        numbers[idx] = tmp
    return numbers


if __name__ == "__main__":
    result = bubble_sort(numbers=[9, 2, 1, 5, 7, 3, 8, 4, 6, 0])
    print(f"Bubble Sort: {result}")
    print("------------------------")

    result = selection_sort(numbers=[9, 2, 1, 5, 7, 3, 8, 4, 6, 0])
    print(f"Selection Sort: {result}")
    print("------------------------")
