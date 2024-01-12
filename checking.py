import pytest
from finding import find_second_maximum_matrix

# Test case 1: Positive matrix
def test_valid_input_matrix():
    input_matrix = [
        [1, 5, 3],
        [7, 2, 8],
        [4, 6, 9]
    ]
    result = find_second_maximum_matrix(input_matrix)
    assert result == 9

# Test case 2: Negative numbers
def test_negative_numbers_matrix():
    input_matrix = [
        [-1, -1, -1],
        [-1, -2, -1],
        [-7, -1, -3]
    ]
    result = find_second_maximum_matrix(input_matrix)
    assert result == -2

# Test case 3: Empty matrix
def test_empty_matrix():
    input_matrix = []
    result = find_second_maximum_matrix(input_matrix)
    assert result is -1  

# Test case 4: Duplicate second maximum
def test_duplicate_second_maximum_matrix():
    input_matrix = [
        [3, 5, 8],
        [7, 5, 1],
        [4, 6, 8]
    ]
    result = find_second_maximum_matrix(input_matrix)
    assert result == 7

# Test case 5: Test different size matrix
def test_random_matrix():
    input_matrix = [
        [3, 5, 8],
        [7, 5, 1],
        [4, 6, 8], 
           [0], 
           [-1]
    ]
    result = find_second_maximum_matrix(input_matrix)
    assert result == 7

# Test case 6: Final test
def test_last():
    input_matrix = [[1,2,3],[[4,5,6,[7]],[8,9]]]
    result = find_second_maximum_matrix(input_matrix)
    assert result == 8

if __name__ == "__main__":
    pytest.main()