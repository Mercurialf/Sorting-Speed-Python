# Sorting speed comparison program

import random
import time

__version__ = '0.1'

print('Sorting speed comparison program.\n'
      'ver.{0}\n'.format(__version__))


# Функция сравнения идентичности всех списков
def check_list(default_list):
    first_default_list = default_list[0]
    index = 0
    while True:
        if first_default_list == default_list[index]:
            index += 1
            if index == 5:
                return True
        else:
            return False


# Функция которая создает список из случайных чисел в заданном диапазоне
def create_random_list(len_list=1000, min_nums=0, max_nums=1000):
    index = 0
    nums_list_create = []
    while index < len_list:
        nums_list_create.append(random.randint(min_nums, max_nums))
        index += 1
    print('A list of random numbers has been generated.')
    return nums_list_create


def copy_random_list(nums_list):
    # Создание копий списка
    nums_list_1 = list(nums_list)
    nums_list_2 = list(nums_list)
    nums_list_3 = list(nums_list)
    nums_list_4 = list(nums_list)
    nums_list_5 = list(nums_list)

    nums_list_full = [nums_list_1, nums_list_2, nums_list_3, nums_list_4, nums_list_5]

    if check_list(nums_list_full):
        print('The first and last list are identical.', '\n')
        return nums_list_full
    else:
        print('Error comparing lists.')


# Создание первого списка
first_nums_list = create_random_list()
# print(first_nums_list, len(first_nums_list))

nums_list_verified = copy_random_list(first_nums_list)
# print(nums_list_verified, len(nums_list_verified))


#################################################
# Bubble sort
def bubble_sort(val):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(val) - 1):
            if val[i] > val[i + 1]:
                val[i], val[i + 1] = val[i + 1], val[i]
                swapped = True


#################################################
# Heapsort
def heapify(val, heap_size, root_index):
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    if left_child < heap_size and val[left_child] > val[largest]:
        largest = left_child

    if right_child < heap_size and val[right_child] > val[largest]:
        largest = right_child

    if largest != root_index:
        val[root_index], val[largest] = val[largest], val[root_index]
        heapify(val, heap_size, largest)


def heap_sort(val):
    n = len(val)

    for i in range(n, -1, -1):
        heapify(val, n, i)

    for i in range(n - 1, 0, -1):
        val[i], val[0] = val[0], val[i]
        heapify(val, i, 0)


#################################################
# Quick sort
def partition(nums, low, high):
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1

    while True:

        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j

        nums[i], nums[j] = nums[j], nums[i]


def quick_sort(nums):
    def _quick_sort(items, low, high):
        if low < high:
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)


#################################################
# Sort by inserts
def insertion_sort(nums):
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        j = i - 1

        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = item_to_insert


#################################################
# Sort by selection
def selection_sort(nums):
    for i in range(len(nums)):
        lowest_value_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]


#################################################
def time_sort(nums_list):
    start = time.time()
    bubble_sort(nums_list[0])
    end = time.time()
    print('Bubble sorting was used, time:\n', end - start)

    start = time.time()
    selection_sort(nums_list[1])
    end = time.time()
    print('Selection sorting was used, time:\n', end - start)

    start = time.time()
    insertion_sort(nums_list[2])
    end = time.time()
    print('Insertion sorting was used, time:\n', end - start)

    start = time.time()
    heap_sort(nums_list[3])
    end = time.time()
    print('Heap sorting was used, time:\n', end - start)

    start = time.time()
    quick_sort(nums_list[4])
    end = time.time()
    print('Quick sorting was used, time:\n', end - start)


time_sort(nums_list_verified)
