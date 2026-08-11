"""Verify the core Week 1 scientific Python environment."""

from importlib.metadata import version

import matplotlib
import numpy as np
import pandas as pd


def main() -> None:
    matrix = np.array([[3.0, 1.0], [1.0, 2.0]])
    vector = np.array([9.0, 8.0])
    solution = np.linalg.solve(matrix, vector)

    assert np.allclose(matrix @ solution, vector)

    packages = ("numpy", "pandas", "matplotlib", "jupyterlab", "pytest")
    print("EDSML Week 1 environment check")
    for package in packages:
        print(f"- {package}: {version(package)}")
    print(f"- linear-system solution: {solution.tolist()}")
    print("- status: OK")


if __name__ == "__main__":
    main()

