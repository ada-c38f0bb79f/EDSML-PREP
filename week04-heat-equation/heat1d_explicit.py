"""Explicit finite-difference solver for the one-dimensional heat equation."""

from __future__ import annotations

import numpy as np


def solve_heat_explicit(
    initial: np.ndarray,
    diffusivity: float,
    dx: float,
    dt: float,
    steps: int,
) -> np.ndarray:
    """Return the full time history for fixed-value boundary conditions."""
    raise NotImplementedError("Implement during Week 4")
