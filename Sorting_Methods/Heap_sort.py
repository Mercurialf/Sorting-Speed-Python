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
