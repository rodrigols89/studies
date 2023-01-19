########################################################
# Rodrigo Leite - drigols                              #
# Last update: 17/10/2021                              #
########################################################

from sklearn.preprocessing import StandardScaler

x = [[4, 1, 2, 2], [1, 3, 9, 3], [5, 7, 5, 1]]

normalized = StandardScaler()
print(normalized.fit_transform(x))
