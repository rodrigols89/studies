##########################################################################
# Rodrigo Leite da Silva - drigols                                       #
# Last update: 14/12/2023                                                #
##########################################################################


def heap_permutation(elements):
    if len(elements) == 0:                             # c1, 1 (base case: empty list)
        return [[]]                                    # c2, 1 (return empty list of permutations)

    permutations = []                                  # c3, 1 (initialize empty list for permutations)
    for i in range(len(elements)):                     # c4, n (iterate over each element)
        rest = elements[:i] + elements[i + 1 :]        # c5, 2n (create sub-list without current element)
        sub_permutations = heap_permutation(rest)      # c6, T(n-1) (recursive call with smaller sub-list)
        for perm in sub_permutations:                  # c7, n * T(n-1) (iterate over sub-permutations)
            permutations.append([elements[i]] + perm)  # c8, n * T(n-1) (prepend current element and append to permutations)
    return permutations                                # c9, 1 (return final list of permutations)


if __name__ == "__main__":

    my_elements = [1, 2, 3]
    permutations_list = heap_permutation(my_elements)
    for permutation in permutations_list:
        print(permutation)
