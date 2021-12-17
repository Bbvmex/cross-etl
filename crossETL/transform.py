from random import randint

def quicksort(array):
    if len(array) < 2:
        return array
    else:
        # The array is "random" so pivot can be the first position
        pivot = array[0]
        lower = quicksort([x for x in array[1:] if x < pivot])
        higher = quicksort([x for x in array[1:] if x >= pivot])
        return lower + [pivot] + higher


if __name__ == '__main__':
    array = []
    with open('data.txt', 'r') as inFile:
        for line in inFile:
            array.append(float(line))
    #array = [2,5,8,4,1,6,3,23,6,10]
    sorted = quicksort(array)
    array2 = array.copy()
    array2.sort()