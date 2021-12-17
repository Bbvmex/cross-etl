import pytest

from crossETL.transform import quicksort

def test_sorted(array):
    test_array = []
    with open('data.txt', 'r') as inFile:
        for line in inFile:
            test_array.append(float(line))
    assert quicksort(array) == test_array.sort()
    