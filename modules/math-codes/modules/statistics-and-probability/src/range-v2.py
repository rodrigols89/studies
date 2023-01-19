########################################################
# Rodrigo Leite da Silva - drigols                     #
# Last update: 2022/12/22                              #
########################################################

def find_range(numbers):
    lowest = min(numbers)
    highest = max(numbers)
    r = highest-lowest
    return lowest, highest, r

if __name__ == '__main__':
    donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
    lowest, highest, r = find_range(donations)
    print('Lowest donation: {0} | highest donation: {1} | Range: {2}'.format(lowest, highest, r))
