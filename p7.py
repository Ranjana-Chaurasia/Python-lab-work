# Functional Data Filtering & Matrix Transformation Suite
def filter_negative(matrix):
    filtered_matrix = []
    for row in matrix:
        filtered_row = list(filter(lambda x: x>=0, row))
        filtered_matrix.append(filtered_row)
    return filtered_matrix
def transform_matrix(matrix, multiplier):
    transformed_matrix = []
    for row in matrix:
        filtered_row = list(map(lambda x: x*multiplier, row))
        transformed_matrix.append(filtered_row)
    return transformed_matrix
def sort_entries(entries, index):
    return sorted(entries, key=lambda entry: entry[index], reverse=True)

matrix = [
    [4, -2, 7],
    [3, 6, -5],
    [1, 8, 9]
]
result = filter_negative(matrix)
print("Filtered matrix: ", result)
result = transform_matrix(matrix, 2)
print("Transformed matrix: ", result)
entries = [
    ("Mutya", 97),
    ("Anand", 95),
    ("Monu", 65),
    ("Lattu", 90)
]
result = sort_entries(entries, 1)
print("Sorted entries: ", result)