# Week 1: Imperial Preparation and Toolchain

## Deliverable

Complete the presessional Python, Git, Bash, and mathematics preparation, and
leave this repository ready for reproducible scientific work.

## Checklist

### Toolchain

- [x] Install or verify a supported Python 3 environment.
- [x] Create `.venv` and install `requirements.txt`.
- [x] Launch JupyterLab successfully.
- [ ] Confirm access to the Imperial EDSML presessional JupyterHub.
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

The official page lists the exercises as due on 3 October 2026. Imperial says
it will provide the submission repository during induction week, with details
on 30 September; this preparation repository is not that official submission
repository.

### Command line

- [ ] Complete the Imperial-linked Software Carpentry Bash lesson.
- [ ] Complete the short Linux command-line practice test.
- [ ] Practise navigation, file operations, pipes, redirection, wildcards, and
      searching from a shell.
- [ ] Record whether course work will use JupyterHub, WSL, or another Unix shell
      locally.

### Git

- [x] Explain working tree, staging area, commits, branches, and remotes.
- [x] Make a focused commit from the command line.
- [x] Create and merge a short-lived practice branch.
- [x] Inspect changes with `git status`, `git diff`, and `git log`.
- [ ] Finish the full Imperial-modified Software Carpentry Git lesson,
      including collaboration, conflicts, licensing, citation, and hosting.
- [x] Use the Imperial-issued GitHub username for the course account.

### Mathematics

- [ ] Review vectors, matrices, norms, inner products, and projections.
- [ ] Review matrix multiplication, determinants, inverses, and linear systems.
- [ ] Review eigenvalues/eigenvectors and their numerical interpretation.
- [ ] Review differentiation, integration, extrema, and Taylor series.
- [ ] Review partial derivatives, gradients, vector calculus, and the chain
      rule.
- [ ] Review first- and higher-order ODEs, including separation of variables
      and integrating factors.
- [ ] Review basic PDE concepts, including diffusion, Laplace/Poisson, and wave
      equations.
- [ ] Review probability, conditional probability, expectation, variance, and
      covariance.
- [ ] Review basic trigonometry, algebra, and geometry where needed.
- [ ] Attempt the official mathematics self-check questions before deciding
      which topics need deeper revision.
- [ ] Write down topics that need deeper work in `learning-log.md`.

## Official references

- EDSML pre-induction home:
  https://ese-msc.github.io/preinduction/edsml/markdown/EDSMLIntro.html
- Mathematics self-check and revision:
  https://ese-msc.github.io/preinduction/edsml/markdown/mathsintro.html
- Python material and submission note:
  https://ese-msc.github.io/preinduction/edsml/notebooks/python.html
- Command-line preparation:
  https://ese-msc.github.io/preinduction/edsml/markdown/bashintro.html
- Imperial-modified Git lesson:
  https://ese-msc.github.io/git-novice/
- Optional presessional reading list:
  https://ese-msc.github.io/preinduction/edsml/markdown/edsml_reading_list.html

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
