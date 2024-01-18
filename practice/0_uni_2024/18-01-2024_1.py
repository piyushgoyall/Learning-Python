import numpy as np

# Define two matrices: one with determinant zero and one with a non-zero determinant
matrix_singular = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  # This matrix is singular (determinant zero)

matrix_non_singular = np.array([[2, 3, 4], [1, 5, 7], [3, 1, 6]])  # This matrix is non-singular (determinant non-zero)

# Function to compute and return the inverse of a matrix or a message if it's singular
def compute_inverse(matrix):
    try:
        inv_matrix = np.linalg.pinv(matrix)
        return inv_matrix
    except np.linalg.LinAlgError:
        return "The matrix is singular and cannot be inverted."

# Compute inverses for both matrices
inverse_singular = compute_inverse(matrix_singular)
inverse_non_singular = compute_inverse(matrix_non_singular)

print(inverse_singular)
print(inverse_non_singular)


# import numpy as np

# # Define two matrices: one with determinant zero and one with a non-zero determinant
# matrix_singular = np.array([[1, 2, 3],
#                             [4, 5, 6],
#                             [7, 8, 9]])  # This matrix is singular (determinant zero)

# matrix_non_singular = np.array([[2, 3, 4],
#                                 [1, 5, 7],
#                                 [3, 1, 6]])  # This matrix is non-singular (determinant non-zero)

# # Function to compute and return the inverse of a matrix or a message if it's singular
# def compute_inverse(matrix):
#     try:
#         inv_matrix = np.linalg.inv(matrix)
#         return inv_matrix
#     except np.linalg.LinAlgError:
#         return "The matrix is singular and cannot be inverted."

# # Compute inverses for both matrices
# inverse_singular = compute_inverse(matrix_singular)
# inverse_non_singular = compute_inverse(matrix_non_singular)

# inverse_singular, inverse_non_singular