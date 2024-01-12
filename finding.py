def find_second_maximum_matrix(matrix):
    if not matrix or not matrix[0]:
        return None  # Return None for an empty matrix or empty rows

    max_values = set()

    for row in matrix:
        if len(row) > 1:
            max_values.add(max(row))

    if len(max_values) < 2:
        return None  # Return None if there are not enough unique maximum values

    max_values.remove(max(max_values))  # Remove the overall maximum to get the second maximum
    return max(max_values)