import pytest

import random
from crossETL.transform import quicksort

@pytest.fixture
def test_array():
    return [random.uniform(0,10) for i in range(10000)]

@pytest.fixture
def ordered_array(test_array):
    ordered_array = test_array.copy()
    ordered_array.sort()
    return ordered_array

def test_quicksort(test_array, ordered_array):
    assert quicksort(test_array) == ordered_array

def test_not_initially_ordered(test_array):
    assert quicksort(test_array) != test_array



    