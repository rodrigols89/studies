##########################################################################
# Rodrigo Leite da Silva - drigols                                       #
# Last update: 14/12/2023                                                #
##########################################################################


def merge_sort(data):
    if len(data) <= 1:                                                    # c1, 1
        return                                                            # c2, 1
    
    mid = len(data) // 2                                                  # c3, 1
    left_data = data[:mid]                                                # c4, n/2
    right_data = data[mid:]                                               # c5, n/2

    merge_sort(left_data)                                                 # c6, T(n/2)
    merge_sort(right_data)                                                # c7, T(n/2)

    left_index = 0                                                        # c8, 1
    right_index = 0                                                       # c9, 1
    data_index = 0                                                        # c10, 1

    while left_index < len(left_data) and right_index < len(right_data):  # c11, n
        if left_data[left_index] < right_data[right_index]:               # c12, n
            data[data_index] = left_data[left_index]                      # c13, n
            left_index += 1                                               # c14, n
        else:                                                             # c15, n
            data[data_index] = right_data[right_index]                    # c16, n
            right_index += 1                                              # c17, n
        data_index += 1                                                   # c18, n
    
    if left_index < len(left_data):                                       # c19, 1
        del data[data_index:]                                             # c20, 1
        data += left_data[left_index:]                                    # c21, n
    elif right_index < len(right_data):                                   # c22, 1
        del data[data_index:]                                             # c23, 1
        data += right_data[right_index:]                                  # c24, n

if __name__ == '__main__':
    data = [9, 1, 7, 6, 2, 8, 5, 3, 4, 0]
    merge_sort(data)
    print(data)
