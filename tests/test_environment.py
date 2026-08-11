import numpy as np


def test_linear_system_solution() -> None:
    matrix = np.array([[3.0, 1.0], [1.0, 2.0]])
    vector = np.array([9.0, 8.0])

    solution = np.linalg.solve(matrix, vector)

    assert np.allclose(solution, np.array([2.0, 3.0]))

