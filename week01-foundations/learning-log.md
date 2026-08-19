# Week 1 Learning Log

## Session

**Date:** 2026-07-28

### Completed

- Created the EDSML preparation repository structure.
- Added a reproducible Python environment specification and automated check.
- Converted the Week 1 deliverable into an acceptance checklist.
- Completed the introductory NumPy learning session.
- Created `numpy_basics.ipynb` with examples and independent exercises.
- Completed all exercises in Imperial `lecture1/lecture1.ipynb`.
- Completed all exercises in Imperial `lecture2/lecture2.ipynb`.

### Notes

- Python:
  - Distinguished Python list repetition from NumPy element-wise operations.
  - Used vectorised arithmetic instead of explicit loops.
  - Created Boolean masks and used them for filtering and assignment.
  - Excluded explicit missing-value sentinels without discarding valid negative
    environmental measurements.
  - Used `shape`, two-dimensional indexing, and slicing with the
    `array[rows, columns]` convention.
  - Applied `axis=0` for column-wise statistics and `axis=1` for row-wise
    statistics.
  - Learned how broadcasting aligns dimensions and why `[:, None]` converts a
    one-dimensional array into a column of shape `(n, 1)`.
  - Used `np.isnan`, `np.isfinite`, `np.nanmean`, and other NaN-aware
    statistics.
  - Recognised that Boolean indexing a two-dimensional array normally flattens
    the selected values and loses the row/column structure.
  - Practised pandas column selection, Boolean filtering, `.loc`, derived
    columns, grouped aggregation, missing-value handling, sorting, duplicate
    handling, date fields, and pivot tables.
  - Confirmed prior familiarity with core Python functions and Matplotlib.
  - Practised list mutation, `enumerate`, `zip`, nested lists, tuples, and
    conditional expressions.
  - Implemented numerical loops for factorials, path lengths, prime sieving,
    and polygon-based approximation.
  - Used NumPy vectorisation, slicing, Boolean indexing, reshaping, and
    multidimensional array traversal.
  - Implemented matrix-vector and matrix-matrix multiplication from their
    index definitions and compared them with NumPy's `@` operator.
- Git:
- Mathematics:

### Questions and gaps

- Continue checking array shapes before broadcasting.
- Practise choosing between Boolean filtering and NaN-aware reductions.
- Complete the independent exercises in `numpy_basics.ipynb`.

### Next session

1. Complete Imperial presessional Lecture 3.
2. Continue through compulsory Lectures 4-5.
3. Record any concepts that need revision after each lecture.
