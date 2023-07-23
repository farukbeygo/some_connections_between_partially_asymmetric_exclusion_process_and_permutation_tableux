import numpy as np


def passe_generator(size):
    m_size = 2**size
    matrix = np.zeros((m_size, m_size))

    for i in range(m_size):
        for j in range(m_size):
            if i == j:
                matrix[i][j] = 1

    return matrix


N = 3
print(passe_generator(N))
