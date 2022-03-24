def bubble_sort(val):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(val) - 1):
            if val[i] > val[i + 1]:
                val[i], val[i + 1] = val[i + 1], val[i]
                swapped = True
