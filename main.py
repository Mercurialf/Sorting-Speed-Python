# Sorting speed comparison program

import random
import time
from Sorting_Methods import Bubble_sort
from Sorting_Methods import Heap_sort
from Sorting_Methods import Quick_sort
from Sorting_Methods import Inserts_sort
from Sorting_Methods import Selection_sort

__version__ = '0.1'

print('Sorting speed comparison program.\n'
      'ver.{0}\n'.format(__version__))


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


def create_random_list(len_list=1000, min_nums=0, max_nums=1000):
    index = 0
    nums_list_create = []
    while index < len_list:
        nums_list_create.append(random.randint(min_nums, max_nums))
        index += 1
    print('A list of random numbers has been generated.')
    return nums_list_create


def copy_random_list(nums_list):
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


first_nums_list = create_random_list()
nums_list_verified = copy_random_list(first_nums_list)


def time_sort(nums_list):
    start = time.time()
    Bubble_sort.bubble_sort(nums_list[0])
    end = time.time()
    print('Bubble sorting was used, time:\n', end - start)

    start = time.time()
    Selection_sort.selection_sort(nums_list[1])
    end = time.time()
    print('Selection sorting was used, time:\n', end - start)

    start = time.time()
    Inserts_sort.insertion_sort(nums_list[2])
    end = time.time()
    print('Insertion sorting was used, time:\n', end - start)

    start = time.time()
    Heap_sort.heap_sort(nums_list[3])
    end = time.time()
    print('Heap sorting was used, time:\n', end - start)

    start = time.time()
    Quick_sort.quick_sort(nums_list[4])
    end = time.time()
    print('Quick sorting was used, time:\n', end - start)


time_sort(nums_list_verified)
