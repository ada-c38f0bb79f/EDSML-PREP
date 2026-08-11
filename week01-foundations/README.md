# Week 1: Imperial Preparation and Toolchain

## Deliverable

Complete the presessional Python, Git, and mathematics preparation, and leave
this repository ready for reproducible scientific work.

## Checklist

### Toolchain

- [x] Install or verify a supported Python 3 environment.
- [x] Create `.venv` and install `requirements.txt`.
- [x] Launch JupyterLab successfully.
- [x] Configure `git config user.name` and `git config user.email`.
- [x] Run the automated environment check.

### Python

- [x] Review values, control flow, functions, modules, and exceptions.
- [x] Practise NumPy arrays, indexing, broadcasting, and vectorisation.
- [x] Practise pandas loading, filtering, grouping, and missing-data handling.
- [x] Create at least one clear Matplotlib figure with labels and units.
- [ ] Complete the assigned Imperial presessional Python exercises.

#### Imperial presessional course

The official course is stored in
[`imperial-introduction-to-python`](imperial-introduction-to-python/README.md).
Open `imperial-introduction-to-python/index.ipynb`, then complete lectures 1-5
in order. Lecture 6 is optional.

Do not rename exercise variables, functions, or classes, and do not edit the
PyBryt or `assert` test cells. The Imperial exercise item is complete when all
compulsory exercise tests in lectures 1-5 pass.

### Git

- [x] Explain working tree, staging area, commits, branches, and remotes.
- [x] Make a focused commit from the command line.
- [x] Create and merge a short-lived practice branch.
- [x] Inspect changes with `git status`, `git diff`, and `git log`.

### Mathematics

- [ ] Review vectors, matrices, norms, inner products, and projections.
- [ ] Review derivatives, gradients, Jacobians, and the chain rule.
- [ ] Review probability distributions, expectation, variance, and covariance.
- [ ] Review eigenvalues/eigenvectors and their numerical interpretation.
- [ ] Write down topics that need deeper work in `learning-log.md`.

## Environment check

With the virtual environment activated, run:

```powershell
python week01-foundations/check_environment.py
python -m pytest
```

The check prints installed package versions and performs a small numerical
calculation. Both commands must finish without errors.

## Definition of done

- Every applicable checklist item above is checked.
- The Imperial exercises are complete or linked from `learning-log.md`.
- `check_environment.py` and the tests pass.
- `learning-log.md` records what was learned, remaining gaps, and next steps.
- The repository has a readable history of focused commits.
