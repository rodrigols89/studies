##########################################################################
# Rodrigo Leite da Silva - drigols                                       #
# Last update: 14/12/2023                                                #
##########################################################################


def linear_search(data, value):
    for index in range(len(data)):                   # c1, n
        if value == data[index]:                     # c2, n
            return index                             # c3, 1
    raise ValueError('Value not found in the list')  # c4, 1

if __name__ == '__main__':
    data = [1, 2, 9, 8, 3, 4, 7, 6, 5]
    print(linear_search(data, 7))
