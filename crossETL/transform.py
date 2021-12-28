from random import randint

def quicksort(array):
    '''Simple implementation of Quicksort
    As the array is "random", the pivot is the first element
    (If the array is already a little sorted, it would be the worst case scenario)
    Worst case: O(n²) / Average: O(n*log n)'''
    
    if len(array) < 2:
        return array
    else:
        # The array is "random" so pivot can be the first position
        pivot = array[0]
        lower = quicksort([x for x in array[1:] if x < pivot])
        higher = quicksort([x for x in array[1:] if x >= pivot])
        return lower + [pivot] + higher


if __name__ == '__main__':
    import csv
    array = []
    with open('crossETL/data.txt', 'r') as inFile:
        for line in inFile:
            array.append(float(line))
    #array = [2,5,8,4,1,6,3,23,6,10]
    sorted = quicksort(array)
    with open('crossETL/data_sorted.csv', 'w') as outFile:
        writer = csv.writer(outFile)
        writer.writerow(sorted)