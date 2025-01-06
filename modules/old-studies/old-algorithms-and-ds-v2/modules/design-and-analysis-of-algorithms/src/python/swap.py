##########################################################################
# Rodrigo Leite da Silva - drigols                                       #
# Last update: 14/12/2023                                                #
##########################################################################

def swap_variables(x, y):
    x = x + y    # c1, 1
    y = x - y    # c2, 1
    x = x - y    # c3, 1
    return x, y  # c4, 1

if __name__ == "__main__":

    x = 10
    y = 5
    print(f"Before Swapping: x = {x}, y = {y}")

    x, y = swap_variables(x, y)
    print(f"After Swapping: x = {x}, y = {y}")
