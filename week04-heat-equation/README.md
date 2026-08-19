# Week 4: Numerical PDE Solver - 1D Heat Equation

## Deliverables

- `heat1d_explicit.py`
- `heat1d_implicit.py`
- `experiments.ipynb`
- A stability experiment comparing observed and theoretical behaviour.

## Checklist

- [ ] State the PDE, domain, initial condition, and boundary conditions.
- [ ] Derive the finite-difference stencil.
- [ ] Implement an explicit solver with input validation.
- [ ] Implement an implicit solver using a linear solve.
- [ ] Verify both solvers against an analytical or manufactured solution.
- [ ] Run grid-refinement and time-step experiments.
- [ ] Demonstrate the explicit stability threshold.
- [ ] Add focused automated tests.

## Official resources and format

- MIT numerical methods/PDE material (notes and notebooks):
  https://github.com/mitmath/numerical_hub
- MIT 18.336 fast PDE methods (readings; coursework uses notebooks):
  https://github.com/mitmath/18336
- Imperial Maldives FEM training (10 notebooks; no explicit repository
  license, so link only):
  https://github.com/ImperialCollegeLondon/maldives-fem-training
- Imperial Mathematical Computing Demo (notebooks; MIT):
  https://github.com/ImperialCollegeLondon/Mathematical-Computing-Demo

The local `.py` files are the reusable solver implementation. The notebook is
for derivation, experiments, plots, and interpretation.
