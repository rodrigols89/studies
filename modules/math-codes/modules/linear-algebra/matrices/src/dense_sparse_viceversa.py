########################################################
# Rodrigo Leite - drigols                              #
# Last update: 02/03/2021                              #
########################################################

from scipy.sparse import csr_matrix
from numpy import array

# Create dense matrix
dense_matrix = array(
  [
    [1, 0, 0, 1, 0, 0],
    [0, 0, 2, 0, 0, 1],
    [0, 0, 0, 2, 0, 0]
  ]
)

# Convert to sparse matrix (CSR method)
sparse_matrix = csr_matrix(dense_matrix)
print("Sparse Matrix:\n", sparse_matrix)
print("Sparse Matrix shape:", sparse_matrix.shape)

# Reconstruct dense matrix
dense_matrix_two = sparse_matrix.todense()
print("\nDense Matrix:\n", dense_matrix_two)
print("Dense Matrix shape:\n", dense_matrix_two.shape)
