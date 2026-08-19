# Week 7: Scientific Machine Learning / PINN

## Deliverable

Complete `heat_equation_pinn.ipynb`: solve the same heat-equation problem used
in Week 4 with a PINN and compare it against the finite-difference reference.

## Checklist

- [ ] Define the network inputs, output, domain, and normalisation.
- [ ] Compute the PDE residual with automatic differentiation.
- [ ] Include initial and boundary-condition losses.
- [ ] Document sampling and loss weights.
- [ ] Train reproducibly and plot loss components.
- [ ] Compare predictions with the Week 4 reference on a shared grid.
- [ ] Report quantitative error and runtime/training cost.
- [ ] Discuss failure modes and sensitivity.

## Official resources and format

- DeepXDE (mostly Python example scripts; LGPL-2.1):
  https://github.com/lululxvi/deepxde
- DeepXDE heat-equation example:
  https://github.com/lululxvi/deepxde/blob/master/examples/pinn_forward/heat.py
- SciML NeuralPDE.jl (Julia source and documentation, no notebooks):
  https://github.com/SciML/NeuralPDE.jl
- MIT Applications of Scientific Machine Learning (notes/code):
  https://github.com/mitmath/18S096SciML
- PyTorch tutorials:
  https://pytorch.org/tutorials/

The local notebook provides one coherent Python workflow because the primary
references mix Python scripts, Julia examples, and documentation.
