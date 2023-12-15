##########################################################################
# Rodrigo Leite da Silva - drigols                                       #
# Last update: 14/12/2023                                                #
##########################################################################


def binary_search(data, value):
    n = len(data)                                 # c1,  1
    left = 0                                      # c2,  1
    right = n - 1                                 # c3,  1
    while left <= right:                          # c4,  log2(n) + 1
        middle = (left + right) // 2              # c5,  log2(n)
        if value < data[middle]:                  # c6,  1
            right = middle - 1                    # c7,  1
        elif value > data[middle]:                # c8,  1
            left = middle + 1                     # c9,  1
        else:                                     # c10, 1
            return middle                         # c11, 1
    raise ValueError('Value is not in the list')  # c12, 1

if __name__ == '__main__':

    data1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    value1 = 6
    result1 = binary_search(data1, value1)
    print(f"Binary Search Result: {result1}")

    data2 = ['apple', 'banana', 'cherry', 'grape', 'orange']
    value2 = 'cherry'
    result2 = binary_search(data2, value2)
    print(f"Binary Search Result: {result2}")

    data3 = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    value3 = 0.5
    result3 = binary_search(data3, value3)
    print(f"Binary Search Result: {result3}")

    data4 = []
    value4 = 42
    try:
        result4 = binary_search(data4, value4)
        print(f"Binary Search Result: {result4}")
    except ValueError as e:
        print(f"Binary Search Result: {e}")
