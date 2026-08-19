# Week 5: Diffusion Inverse Problem

## Deliverable

Complete `diffusion_inversion.ipynb`: generate or load observations, infer the
diffusion coefficient, quantify fit quality, and discuss identifiability.

## Checklist

- [ ] Reuse the tested Week 4 forward model.
- [ ] Define observation locations, times, and noise assumptions.
- [ ] Define a scalar objective function.
- [ ] Estimate diffusivity with `scipy.optimize`.
- [ ] Compare true/estimated parameters and predicted observations.
- [ ] Examine sensitivity to noise and initial guess.
- [ ] Discuss bounds, regularisation, uncertainty, and non-uniqueness.

## Official resources and format

- SciPy optimisation API (documentation and Python examples):
  https://docs.scipy.org/doc/scipy/reference/optimize.html
- DeepXDE (primarily Python scripts; LGPL-2.1):
  https://github.com/lululxvi/deepxde
- DeepXDE inverse diffusion example:
  https://github.com/lululxvi/deepxde/blob/master/examples/pinn_inverse/diffusion_1d_inverse.py
- MIT Scientific Machine Learning course (notes and code):
  https://github.com/mitmath/18S096SciML

This week is locally notebook-based even though the DeepXDE reference examples
are mainly `.py` scripts.
