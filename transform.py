from random import randint

def quicksort(array):
    if len(array) < 2:
        return array
    lower = []
    equal = []
    higher = []

    pivot = array[int(len(array)/2)]

    for item in array:
        if item < pivot:
            lower.append(item)
        elif item == pivot:
            equal.append(item)
        elif item > pivot:
            higher.append(item)
        else:
            print ('Error - Item does not match criteria')

    sorted_lower = quicksort(lower)
    sorted_higher = quicksort(higher)

    return sorted_lower + equal + sorted_higher


if __name__ == '__main__':
    array = [randint(0,1000) for i in range(1000)]
    sorted = quicksort(array)