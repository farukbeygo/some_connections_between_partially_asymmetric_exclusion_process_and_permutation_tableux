import numpy as np


def find_stationary_distribution(a, b, q):
    P = np.array([[1 - a / 3, a / 3, 0, 0],
                  [0, 2 / 3, 1 / 3, 0],
                  [b / 3, q / 3, 1 - b / 3 - a / 3 - q / 3, a / 3],
                  [0, b / 3, 0, 1 - b / 3]])

    # Transpose P to use column vectors (required by np.linalg.eig)
    P_transpose = P.T

    # Find the left eigenvector associated with eigenvalue 1
    eigenvalues, eigenvectors = np.linalg.eig(P_transpose)
    stationary_distribution = eigenvectors[:, np.isclose(eigenvalues, 1)]
    stationary_distribution /= stationary_distribution.sum()

    return stationary_distribution.flatten()


# Example usage with a = 0.5, b = 0.3, and q = 0.2
a_value = 0.5
b_value = 0.3
q_value = 0.2

stationary_distribution = find_stationary_distribution(a_value, b_value, q_value)
print("Stationary Distribution:", stationary_distribution)
